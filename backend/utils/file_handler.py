# utils/file_handler.py

import os
import uuid

ALLOWED_EXTENSIONS = {".txt", ".csv", ".vcf"}
UPLOAD_FOLDER = "uploaded_files"

def save_upload_file(upload_file, destination_folder=UPLOAD_FOLDER):
    os.makedirs(destination_folder, exist_ok=True)

    _, ext = os.path.splitext(upload_file.filename)
    if ext.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {ext}")

    unique_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(destination_folder, unique_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path
