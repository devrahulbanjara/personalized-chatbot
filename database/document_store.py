from typing import List, Union
from parser.document_parser import Parser


class DocumentStore:
    def __init__(self):
        self.parsed_document: Union[str, List[str], None] = None
        self.chunks: List[str] = []

    def load_chunks(
        self, document_path, chunk_size: int = 512, overlap_size: int = 100
    ) -> List[str]:
        parser = Parser()
        self.parsed_document = parser.parse_document(filename=document_path)
        self.chunks = self.chunk_and_overlap(chunk_size, overlap_size)
        return self.chunks

    def chunk_and_overlap(
        self, chunk_size: int = 512, overlap_size: int = 100
    ) -> List[str]:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        if overlap_size < 0:
            raise ValueError("overlap_size must be non-negative")
        if overlap_size >= chunk_size:
            raise ValueError("overlap_size must be less than chunk_size")

        if not self.parsed_document:
            raise ValueError("Document not parsed. Call load_chunks() first.")

        if isinstance(self.parsed_document, list):
            full_text = " ".join(self.parsed_document)
        else:
            full_text = self.parsed_document

        text_length = len(full_text)
        if text_length <= chunk_size:
            return [full_text]

        chunks = []
        start = 0

        while start < text_length:
            end = min(start + chunk_size, text_length)
            chunk = full_text[start:end]
            chunks.append(chunk)
            if end == text_length:
                break
            start = end - overlap_size

        return chunks
