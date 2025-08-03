from PIL import Image

def crop_image(input_path, output_path, crop_box):
    """
    Crops the image based on the given crop_box and saves it to output_path.

    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the cropped image.
        crop_box (tuple): A 4-tuple (left, upper, right, lower).
    """
    img = Image.open(input_path)
    cropped = img.crop(crop_box)
    cropped.save(output_path)
    print(f"Cropped image saved to: {output_path}")

# Example usage
# Crop box format: (left, top, right, bottom)
x = int(input("Enter left coordinate: "))
y = int(input("Enter top coordinate: "))
width = int(input("Enter width: "))
height = int(input("Enter height: "))
crop_image("input.jpg", "cropped.jpg", (x, y, width, height))
