from PIL import Image

def jpg_to_pdf(input_jpg, output_pdf):
    """
    Convert a JPG image to a PDF file.

    :param input_jpg: Path to the input JPG file.
    :param output_pdf: Path where the output PDF will be saved.
    """
    
    try:
        # Open the JPG image
        image = Image.open(input_jpg)
        
        # Convert the image to RGB mode if it is not already
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Save the image as a PDF
        image.save(output_pdf, "PDF", resolution=100.0)
        print(f"Successfully converted {input_jpg} to {output_pdf}")
    
    except Exception as e:
        print(f"An error occurred: {e}")