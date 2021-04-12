import nltk
import pdfplumber

with pdfplumber.open(chosen_file) as pdf:
    first_page = pdf.pages[0]
pdf_paragraphs = first_page.extract_text()
sentences = pdf_paragraphs.split()