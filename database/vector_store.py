import chromadb
import os
from dotenv import load_dotenv
import uuid
from typing import List
import logging

load_dotenv()

logger = logging.getLogger(__name__)


class VectorStore:
    def __init__(self, database_path):
        self.index_name = "adex-chatbot-test"
        self.chroma_client = chromadb.PersistentClient(database_path)
        self.collection = self.chroma_client.get_or_create_collection(
            name="adex_chatbot"
        )

    def add_documents(self, chunks: List[str]):
        ids = [str(uuid.uuid4()) for _ in chunks]
        self.collection.upsert(documents=chunks, ids=ids)

    def query(self, query_text: str, top_k=5):
        results = self.collection.query(
            query_texts=[query_text],
            n_results=top_k,
        )
        logger.debug(results)
        return results
