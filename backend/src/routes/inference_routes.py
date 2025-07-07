from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.orchestration import ChatbotOrchestrator

router = APIRouter()

orchestrator = ChatbotOrchestrator()


class ChatRequest(BaseModel):
    query: str
    session_id: str


@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        relevant_chunks = orchestrator.retrieve_relevant_chunks(request.query)
        response = orchestrator.generate_response(
            request.session_id, request.query, relevant_chunks
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during chat processing: {str(e)}"
        )


@router.get("/healthz", tags=["Health"])
async def health_check():
    return {"status": "ok"}
