from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Failed to add {pdf}: {e}")
    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved to: {output_path}")

# Example usage
pdf_files = [
    "AppointmentLetter_1991162_2021-2022.pdf",
    "May.pdf",
    "Jun.pdf",
    "Jul2025.pdf"
]

output_file = "C:\\Users\\atharv\\Downloads\\PRJ2025dummy\\experience_letter.pdf"
merge_pdfs(pdf_files, output_file)
