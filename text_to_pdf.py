from fpdf import FPDF

def text_to_pdf(text, pdf_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in text.splitlines():
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(pdf_filename)

def pdf_to_text(pdf_filename):
    from PyPDF2 import PdfReader

    reader = PdfReader(pdf_filename)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text