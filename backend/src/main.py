import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.inference_routes import router as inference_router, orchestrator
from src.routes.load_documents_routes import router as load_documents_router
import logging
import sys
import asyncio

log_formatter = logging.Formatter(
    "[%(asctime)s] | [%(levelname)-8s] | [%(name)-25s] | %(message)s"
)
logger = logging.getLogger()

if logger.hasHandlers():
    logger.handlers.clear()

logger.setLevel(logging.INFO)

# Console handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)


app = FastAPI(title="Personal Chatbot API")


@app.on_event("startup")
async def startup_event():
    logger.info("Starting background task for session cleanup...")
    asyncio.create_task(orchestrator.cleanup_stale_sessions())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(inference_router, prefix="/api", tags=["Inference"])
app.include_router(load_documents_router, prefix="/api", tags=["Document Loading"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the the chatbot api made by Rahul Dev Banjara"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
