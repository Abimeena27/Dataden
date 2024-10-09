import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

S3_BUCKET = 'datadenfolder'
S3_REGION = 'ap-south-1'
S3_ACCESS_KEY = '**************'
S3_SECRET_KEY = '*************'

# Initialize AWS S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=S3_ACCESS_KEY,
                  aws_secret_access_key=S3_SECRET_KEY,
                  region_name=S3_REGION)

def create_s3_folder(folder_name):
    try:
        # Create a placeholder object to represent the folder
        s3.put_object(Bucket=S3_BUCKET, Key=f'{folder_name}/')
        return {'message': f'Folder "{folder_name}" created in S3 bucket'}, 200
    except Exception as e:
        return {'error': str(e)}, 500

def upload_folder_to_s3(folder_name, files):
    if folder_name == '/':
        folder_name = ''  
    try:
        for file in files:
            file_path = f"{folder_name}/{file.filename}"
            s3.upload_fileobj(file, S3_BUCKET, file_path)
        return True, "Files uploaded successfully"
    except NoCredentialsError:
        return False, "Credentials not available"
    except Exception as e:
        return False, str(e)

def upload_file_to_s3(file_obj, file_name):
    try:
        s3.upload_fileobj(file_obj, S3_BUCKET, file_name)
        return f'File {file_name} uploaded successfully'
    except (NoCredentialsError, PartialCredentialsError) as e:
        return f'Credentials error: {str(e)}'
    except ClientError as e:
        return f'AWS ClientError: {str(e)}'
    except Exception as e:
        return f'Error: {str(e)}'
