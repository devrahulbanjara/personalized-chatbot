from dotenv import load_dotenv
import os
from groq import Groq
from prompts.chatbot_prompt import PROMPT
from collections.abc import Iterable

load_dotenv()

class ChatbotModel:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.history = []
        self.max_history = 3

    def format_history(self):
        history_text = ""
        for user_msg, bot_msg in self.history[-self.max_history:]:
            history_text += f"User: {user_msg}\nAssistant: {bot_msg}\n"
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

    def generate_response(self, query, relevant_chunks):
        if not relevant_chunks:
            return "I'm sorry, but I couldn't find enough information to answer your question at the moment. Please feel free to contact our support team for further assistance."

        relevant_chunks = self.flatten_chunks(relevant_chunks)
        history_text = self.format_history()
        
        prompt = PROMPT.format(
            chat_history=history_text,
            retrieved_chunks="\n".join(relevant_chunks),
        )

        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": query
                }
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

        self.history.append((query, response_text.strip()))

        print("\n" + "="*60)
        print("Conversation History")
        print("="*60)
        for i, (user_msg, bot_msg) in enumerate(self.history, 1):
            print(f"\nConversation {i}:")
            print(f"  User     : {user_msg}")
            print(f"  Assistant: {bot_msg}")
        print("="*60 + "\n")

        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]

        return response_text.strip()
