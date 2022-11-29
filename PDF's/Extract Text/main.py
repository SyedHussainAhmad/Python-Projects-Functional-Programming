from PyPDF2 import PdfReader

if __name__ == "__main__":
    
    reader = PdfReader("Goosebumps.pdf")
    page = reader.pages[7]
    print(page.extract_text())