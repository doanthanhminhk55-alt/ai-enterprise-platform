from fastapi import APIRouter, UploadFile
import shutil

from app.rag.rag_pipeline import process_pdf

router = APIRouter()

@router.post("/upload")

async def upload_pdf(file: UploadFile):

    file_path = f"app/uploads/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    process_pdf(file_path)

    return {
        "message": "PDF uploaded successfully"
    }