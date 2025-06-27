from database.document_store import DocumentStore
from database.vector_store import VectorStore
import os
import logging

logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or "database/chromadb_file"
        os.makedirs(self.db_path, exist_ok=True)
        self.documentstore = DocumentStore()
        self.vector_store = VectorStore(self.db_path)

    def load_document(self, doc_path):
        logger.info(f"Creating a vector documents with {doc_path}")
        chunks = self.documentstore.load_chunks(document_path=doc_path)
        logger.info(f"Extracted {len(chunks)} chunks from the document.")
        self.vector_store.add_documents(chunks)
        logger.info("Chunks successfully stored in ChromaDB vector store.")

    def retrieve_relevant_queries(self, query):
        results = self.vector_store.query(query)
        return results["documents"]


if __name__ == "__main__":
    db = DatabaseManager()
    db.load_document("")
    result = db.retrieve_relevant_queries(
        "Can you tell me what is the Late Fee in the given document"
    )
    breakpoint()
