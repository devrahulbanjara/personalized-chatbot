import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.inference_routes import router as inference_router
from src.routes.load_documents_routes import router as load_documents_router
import logging
import sys

# --- Logging Configuration ---
log_formatter = logging.Formatter(
    "[%(asctime)s] | [%(levelname)-8s] | [%(name)-25s] | %(message)s"
)
logger = logging.getLogger()

# Clear existing handlers to prevent duplicate logs
if logger.hasHandlers():
    logger.handlers.clear()

logger.setLevel(logging.INFO)

# Console handler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
# -----------------------------


app = FastAPI(title="Personal Chatbot API")

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(inference_router, prefix="/api", tags=["Inference"])
app.include_router(load_documents_router, prefix="/api", tags=["Document Loading"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Personal Chatbot API"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
