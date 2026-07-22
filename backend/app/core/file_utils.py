import os
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile

UPLOAD_DIR = Path("storage/uploads")

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def save_uploaded_file(file: UploadFile) -> tuple[str, str]:
    """
    Saves the uploaded file and returns:
    (unique_filename, full_file_path)
    """

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type.",
        )

    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = UPLOAD_DIR / unique_filename

    contents = file.file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 10 MB.",
        )

    with open(file_path, "wb") as f:
        f.write(contents)

    return unique_filename, str(file_path)