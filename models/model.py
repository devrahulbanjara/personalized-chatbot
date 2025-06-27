from dotenv import load_dotenv
import os
from prompts.chatbot_prompt import PROMPT
from google import genai
from collections.abc import Iterable


load_dotenv()


class ChatbotModel:
    def __init__(self):
        self.client = genai.Client()

    def flatten_chunks(self, chunks):
        flattened = []
        for item in chunks:
            if isinstance(item, str):
                flattened.append(item)
            elif isinstance(item, Iterable):
                flattened.extend(self.flatten_chunks(item))
            else:
                flattened.append(str(item))  # in case there are other types
        return flattened

    def generate_response(self, query, relevant_chunks):
        """
        Generate a response based on the provided query.

        Args:
            query (str): The input query for which a response is to be generated.

        Returns:
            str: The generated response.
        """
        if not relevant_chunks:
            return "I don't know."
        # Flatten the chunks in case they are nested
        relevant_chunks = self.flatten_chunks(relevant_chunks)
        prompt = PROMPT.format(
            question=query,
            retrieved_chunks="\n".join(relevant_chunks),
        )
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        return response.text.strip()
