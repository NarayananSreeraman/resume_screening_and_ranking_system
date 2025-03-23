"""import PyPDF2
import docx2txt

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = "".join([page.extract_text() for page in pdf_reader.pages])
    return text

def extract_text_from_docx(docx_file):
    text = docx2txt.process(docx_file)
    return text"""

import PyPDF2
import docx2txt
import io

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file, handling None cases gracefully."""
    text = ""
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_file.read()))
    
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:  # Ensure we don't add None values
            text += page_text + "\n"
    
    return text if text.strip() else "No readable text found in this PDF."

def extract_text_from_docx(docx_file):
    """Extracts text from a DOCX file."""
    return docx2txt.process(docx_file)

