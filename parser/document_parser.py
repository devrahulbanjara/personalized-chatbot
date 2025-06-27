import sys, pathlib, fitz


class Parser:
    def __init__(self):
        pass

    def parse_document(self, filename):
        if filename.endswith(".pdf"):
            pdf_parser = PDFParser()
            return pdf_parser.load_document(filename)


class PDFParser:
    def __init__(self):
        pass

    def load_document(self, filename):
        with fitz.open(filename) as doc:
            text = chr(12).join([page.get_text() for page in doc])
        output_file = pathlib.Path(filename).with_suffix(".txt")
        output_file.write_text(text, encoding="utf-8")
        return text
