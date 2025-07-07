from models.model import ChatbotModel
from database.database import DatabaseManager
import os
import logging

logger = logging.getLogger(__name__)


class ChatbotOrchestrator:
    def __init__(self):
        self.database_path = "data/chromadb_file"
        os.makedirs(self.database_path, exist_ok=True)
        self.db_manager = DatabaseManager()
        self.model = ChatbotModel()

    # Load the document into the vector store
    def load_document(self, doc_path):
        """
        Load a document into the vector store.

        Args:
            doc_path (str): The path to the document to be loaded.
        """
        self.db_manager.load_document(doc_path)

    # Retrieve relevant chunks based on the query
    def retrieve_relevant_chunks(self, query):
        """
        Retrieve relevant chunks from the vector store based on the query.

        Args:
            query (str): The input query for which relevant chunks are to be retrieved.

        Returns:
            List[str]: A list of relevant chunks.
        """
        return self.db_manager.retrieve_relevant_queries(query)

    # Generate a response based on the query and relevant chunks
    def generate_response(self, query, relevant_chunks):
        """
        Generate a response based on the provided query and relevant chunks.

        Args:
            query (str): The input query for which a response is to be generated.
            relevant_chunks (List[str]): A list of relevant chunks to base the response on.

        Returns:
            str: The generated response.
        """
        return self.model.generate_response(query, relevant_chunks)


if __name__ == "__main__":
    orchestrator = ChatbotOrchestrator()
    document_path = "./data/"
    orchestrator.load_document(document_path)

    query = "Can you tell me what is the Late Fee in the given document"
    relevant_chunks = orchestrator.retrieve_relevant_chunks(query)

    response = orchestrator.generate_response(query, relevant_chunks)
    logger.info("Response: %s", response)
