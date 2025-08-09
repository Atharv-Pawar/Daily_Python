import PIL
from PIL import Image
import os

def convert_pdf_to_jpg(pdf_path, output_folder):
    """
    Convert each page of a PDF file to a JPG image.

    :param pdf_path: Path to the input PDF file.
    :param output_folder: Folder where the output JPG images will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF file
    with Image.open(pdf_path) as pdf:
        for page_number in range(pdf.n_frames):
            pdf.seek(page_number)
            jpg_image = pdf.convert("RGB")
            jpg_image.save(os.path.join(output_folder, f"page_{page_number + 1}.jpg"), "JPEG")

def convert_pdf_to_png(pdf_path, output_folder):
    """
    Convert each page of a PDF file to a PNG image.

    :param pdf_path: Path to the input PDF file.
    :param output_folder: Folder where the output PNG images will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF file
    with Image.open(pdf_path) as pdf:
        for page_number in range(pdf.n_frames):
            pdf.seek(page_number)
            png_image = pdf.convert("RGBA")
            png_image.save(os.path.join(output_folder, f"page_{page_number + 1}.png"), "PNG")