from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import tempfile
import os
from src.orchestration import ChatbotOrchestrator

router = APIRouter()


@router.post("/upload-documents")
async def upload_documents(files: List[UploadFile] = File(...)):
    """
    Endpoint to handle document uploads, process them, and store in the vector store.
    """
    orchestrator = ChatbotOrchestrator()
    processed_files = []

    for file in files:
        if not file.filename.lower().endswith((".pdf", ".txt")):
            continue

        try:
            # Use a temporary file to save the uploaded document
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=os.path.splitext(file.filename)[1]
            ) as temp_file:
                content = await file.read()
                temp_file.write(content)
                temp_file.flush()

                # Load the document using the orchestrator
                orchestrator.load_document(temp_file.name)
                processed_files.append(file.filename)

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error processing {file.filename}: {e}"
            )
        finally:
            if "temp_file" in locals() and os.path.exists(temp_file.name):
                os.unlink(temp_file.name)

    if not processed_files:
        raise HTTPException(status_code=400, detail="No valid documents were uploaded.")

    return {
        "status": "success",
        "message": f"Successfully processed {len(processed_files)} documents.",
        "processed_files": processed_files,
    }
