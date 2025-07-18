from dotenv import load_dotenv
import os
from groq import Groq
from prompts.chatbot_prompt import PROMPT
from collections.abc import Iterable

# To load environment variables from a .env file
load_dotenv()


class ChatbotModel:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    def format_history(self, chat_history: list[dict]):
        """Formats the chat history into a string with improved readability."""
        if not chat_history:
            return "No history available."

        history_text = "\n" + "=" * 50 + "\n"  # Add a border for clarity
        history_text += "Chat History:\n"
        history_text += "=" * 50 + "\n"

        for i, message in enumerate(chat_history):
            role = "User" if message["role"] == "user" else "Assistant"
            history_text += f"{'=' * 20}\n"
            history_text += f"{role} ({i+1}):\n"
            history_text += f"{'=' * 20}\n"
            history_text += f"{message['content']}\n"
            history_text += "=" * 50 + "\n"

        return history_text.strip()

    def flatten_chunks(self, chunks):
        flattened = []
        for item in chunks:
            if isinstance(item, str):
                flattened.append(item)
            elif isinstance(item, Iterable):
                flattened.extend(self.flatten_chunks(item))
            else:
                flattened.append(str(item))
        return flattened

    def generate_response(self, query, relevant_chunks, chat_history: list[dict]):
        if not relevant_chunks:
            return "I'm sorry, but I couldn't find enough information to answer your question at the moment. Please feel free to contact our support team for further assistance."

        relevant_chunks = self.flatten_chunks(relevant_chunks)
        history_text = self.format_history(chat_history)
        print(f"\033[1;32m{history_text}\033[0m")  # Print history in green

        prompt = PROMPT.format(
            chat_history=history_text,
            retrieved_chunks="\n".join(relevant_chunks),
        )

        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": query},
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response_text = ""
        for chunk in completion:
            response_text += chunk.choices[0].delta.content or ""

        return response_text.strip()
