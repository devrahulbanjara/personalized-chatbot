from collections import deque
import logging
import asyncio
import time

from models.model import ChatbotModel
from database.database import DatabaseManager
import os

logger = logging.getLogger(__name__)

CHAT_HISTORY_MAX_LENGTH = 4
SESSION_TTL_SECONDS = 3600


class ChatbotOrchestrator:
    def __init__(self):
        self.database_path = "data/chromadb_file"
        os.makedirs(self.database_path, exist_ok=True)
        self.db_manager = DatabaseManager()
        self.model = ChatbotModel()
        self.chat_histories = {}

    def load_document(self, doc_path):
        """
        Load a document into the vector store.

        Args:
            doc_path (str): The path to the document to be loaded.
        """
        self.db_manager.load_document(doc_path)

    def get_chat_history(self, session_id: str):
        """
        Retrieves the chat history for a given session, updating its last access time.
        """
        current_time = time.time()
        if session_id not in self.chat_histories:
            self.chat_histories[session_id] = {
                "history": deque([], maxlen=CHAT_HISTORY_MAX_LENGTH),
                "last_access": current_time,
            }

        self.chat_histories[session_id]["last_access"] = current_time
        return self.chat_histories[session_id]["history"]

    def retrieve_relevant_chunks(self, query: str):
        """
        Retrieve relevant chunks from the vector store based on the query.
        """
        return self.db_manager.retrieve_relevant_queries(query)

    # Generate a response based on the query and relevant chunks
    def generate_response(
        self, session_id: str, query: str, relevant_chunks: list[str]
    ):
        """
        Generate a response and update the chat history for the session.
        """
        chat_history = self.get_chat_history(session_id)

        # Pass the history to the model
        response = self.model.generate_response(
            query, relevant_chunks, list(chat_history)
        )

        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})

        return response

    async def cleanup_stale_sessions(self):
        """Periodically cleans up stale chat sessions."""
        while True:
            await asyncio.sleep(600)
            current_time = time.time()
            stale_sessions = [
                session_id
                for session_id, data in self.chat_histories.items()
                if current_time - data["last_access"] > SESSION_TTL_SECONDS
            ]

            if stale_sessions:
                logger.info(f"Cleaning up {len(stale_sessions)} stale sessions.")
                for session_id in stale_sessions:
                    del self.chat_histories[session_id]
