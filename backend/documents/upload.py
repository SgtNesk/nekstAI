import os
import shutil
from fastapi import UploadFile, File

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "File caricato con successo"}