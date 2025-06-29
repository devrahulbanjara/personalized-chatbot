from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.orchestration import ChatbotOrchestrator

router = APIRouter()

orchestrator = ChatbotOrchestrator()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        relevant_chunks = orchestrator.retrieve_relevant_chunks(request.query)
        if not relevant_chunks:
            response = orchestrator.generate_response(request.query, [])
        else:
            response = orchestrator.generate_response(request.query, relevant_chunks)

        return {"response": response}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during chat processing: {str(e)}"
        )
        
@router.get("/healthz", tags=["Health"])
async def health_check():
    return {"status": "ok"}
