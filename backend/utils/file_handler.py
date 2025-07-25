import os
import uuid
from fastapi import UploadFile
from typing import Literal
import shutil

UPLOAD_DIR = "temp_uploads"
ALLOWED_EXTENSIONS = {".txt", ".csv", ".vcf"}

def ensure_folder_exists(folder_path: str):
    os.makedirs(folder_path, exist_ok=True)

def get_extension(file: UploadFile) -> str:
    _, ext = os.path.splitext(file.filename)
    return ext.lower()

def validate_extension(ext: str):
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"❌ Unsupported file type: {ext}")

async def save_temp_file(file: UploadFile, destination: Literal["temp", "uploads"] = "temp") -> str:
    ext = get_extension(file)
    validate_extension(ext)

    folder = UPLOAD_DIR if destination == "temp" else "uploaded_files"
    ensure_folder_exists(folder)

    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(folder, filename)

    with open(file_path, "wb") as buffer:
        contents = await file.read()
        buffer.write(contents)

    return file_path
