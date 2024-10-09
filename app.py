from flask import Flask, request, jsonify, render_template
from storage import create_s3_folder
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/create-folder', methods=['POST'])
def create_folder():
    folder_name = request.json.get('folderName')

    if not folder_name:
        return jsonify({'error': 'Folder name is required'}), 400

    response, status_code = create_s3_folder(folder_name)
    return jsonify(response), status_code



#if __name__ == '__main__':
 #   app.run(debug=True)
#from flask import Flask, request, jsonify, render_template
from storage import upload_folder_to_s3 , upload_file_to_s3

#app = Flask(__name__)

#@app.route('/')
#def index():
 #   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    folder_name = request.form.get('folderName')
    files = request.files.getlist('files')

    if not folder_name or not files:
        return jsonify({'error': 'Folder name and files are required'}), 400

    success, message = upload_folder_to_s3(folder_name, files)

    if success:
        return jsonify({'message': message}), 200
    else:
        return jsonify({'error': message}), 500

@app.route('/upload-file', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    try:
        response_message = upload_file_to_s3(file, file.filename)
        logger.info(response_message)
        return jsonify({'message': response_message})
    except Exception as e:
        logger.error(f'Error uploading file: {str(e)}')
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)

