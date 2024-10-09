function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const content = document.querySelector('.content');
    sidebar.classList.toggle('closed');
    content.classList.toggle('shifted');
}

function toggleTheme() {
    const body = document.body;
    const sidebar = document.getElementById("sidebar");
    const moonIcon = document.getElementById("moon-icon");
    const sunIcon = document.getElementById("sun-icon");

    body.classList.toggle("dark-theme");
    sidebar.classList.toggle("dark-theme");

    if (body.classList.contains("dark-theme")) {
        moonIcon.style.opacity = "0";
        sunIcon.style.opacity = "1";
    } else {
        moonIcon.style.opacity = "1";
        sunIcon.style.opacity = "0";
    }
}

function openNewFolder() {
    document.getElementById('newFolderModal').style.display = 'block';
}

function closeNewFolder() {
    document.getElementById('newFolderModal').style.display = 'none';
}

function createFolder() {
    const folderName = document.getElementById('folderNameInput').value;
    fetch('/create-folder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ folderName: folderName })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        closeNewFolder();
    });
}

function openFolderUpload() {
    document.getElementById('folderUploadModal').style.display = 'block';
}

function closeFolderUpload() {
    document.getElementById('folderUploadModal').style.display = 'none';
}

function uploadFolder() {
    const form = document.getElementById('uploadForm');
    const formData = new FormData(form);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.message || data.error;
        closeFolderUpload();
    });
}

function openFileUpload() {
    document.getElementById('fileUploadModal').style.display = 'block';
}

function closeFileUpload() {
    document.getElementById('fileUploadModal').style.display = 'none';
}


function uploadFile() {
    const form = document.getElementById('fileUploadForm');
    const formData = new FormData(form);

    fetch('/upload-file', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('fileUploadResponse').innerText = data.message || data.error;
        closeFileUpload();
    });
}
