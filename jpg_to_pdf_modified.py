from PIL import Image
import os

def jpg_to_pdf_under_1mb(input_path, output_path, max_size_kb=1024):
    quality = 95  # Start with high quality
    temp_jpg = "temp_resized.jpg"

    # Open image
    img = Image.open(input_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode for PDF

    while True:
        # Save a temporary resized JPEG
        img.save(temp_jpg, format="JPEG", quality=quality)

        # Convert the compressed JPEG to PDF
        temp_img = Image.open(temp_jpg)
        temp_img.save(output_path, "PDF", resolution=100.0)

        # Check the file size
        size_kb = os.path.getsize(output_path) / 1024
        print(f"Current size: {size_kb:.2f} KB (quality={quality})")

        if size_kb < max_size_kb:
            break

        quality -= 5
        if quality < 10:
            raise Exception("Cannot compress further without significant quality loss.")

    # Cleanup
    if os.path.exists(temp_jpg):
        os.remove(temp_jpg)

# Example usage
jpg_to_pdf_under_1mb("20250727_161658.jpg", "result.pdf")
