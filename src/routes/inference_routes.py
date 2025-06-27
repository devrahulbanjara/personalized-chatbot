from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.orchestration import ChatbotOrchestrator

router = APIRouter()


class ChatRequest(BaseModel):
    query: str


@router.post("/chat")
async def chat(request: ChatRequest):
    """
    Endpoint to handle chat requests and return a response from the chatbot.
    """
    try:
        orchestrator = ChatbotOrchestrator()
        relevant_chunks = orchestrator.retrieve_relevant_chunks(request.query)
        if not relevant_chunks:
            # Handle case where no relevant chunks are found
            # You can return a default message or the query itself to the model
            response = orchestrator.generate_response(request.query, [])
        else:
            response = orchestrator.generate_response(request.query, relevant_chunks)

        return {"response": response}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during chat processing: {str(e)}"
        )
