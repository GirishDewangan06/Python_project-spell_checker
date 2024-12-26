import os
from spellchecker import SpellChecker
from docx import Document
import PyPDF2

def extract_text_from_docx(file_path):
    """Extract text from a Word (.docx) file."""
    try:
        doc = Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return "\n".join(text)
    except Exception as e:
        print(f"Error reading Word file: {e}")
        return ""

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    try:
        text = []
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text.append(page.extract_text())
        return "\n".join(text)
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""

def check_spelling(text):
    """Check spelling of words in the given text."""
    spell = SpellChecker()
    words = text.split()
    misspelled = spell.unknown(words)
    
    corrections = {}
    for word in misspelled:
        corrections[word] = spell.correction(word)
    return corrections

def main():
    file_path = "C:\\Users\\GIRISH\\OneDrive\\Desktop\\spell_check\\pdf_file.pdf"

    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    # Extract text based on file type
    text = ""
    if file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        print("Unsupported file format. Please provide a .docx or .pdf file.")
        return

    # Check if text was extracted successfully
    if not text.strip():
        print("No text found in the file.")
        return

    # Display extracted text 
    print("\nExtracted Text (Preview):\n", text[:500], "...\n")  
    
    corrections = check_spelling(text)
    if corrections:
        print("\nSpelling Corrections:")
        for word, correction in corrections.items():
            print(f"{word} -> {correction}")
    else:
        print("\nNo spelling errors found!")

if __name__ == "__main__":
    main()
