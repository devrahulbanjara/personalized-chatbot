PROMPT = """
You are a helpful assistant specializing in answering questions using provided document excerpts. Answer the question concisely and rely only on the retrieved chunks. Do not copy or quote the chunks directly in your answer. 

If there is not enough information in the chunks to answer, reply clearly that you do not have sufficient information.

Question:
{question}

Retrieved Chunks:
{retrieved_chunks}

Provide a brief, well-structured answer based on these chunks only.
"""
