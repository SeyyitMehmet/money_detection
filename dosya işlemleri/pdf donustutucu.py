import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def image_to_pdf(image_path, output_pdf_path):
    # Create a PDF file with reportlab
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter

    # Open an image file
    with Image.open(image_path) as img:
        # Get the image size
        img_width, img_height = img.size
        # Adjust the image size to fit the page if needed
        aspect = img_width / img_height
        if img_width > width or img_height > height:
            if aspect > (width / height):
                img_width = width
                img_height = width / aspect
            else:
                img_height = height
                img_width = height * aspect

        # Draw the image on the PDF
        c.drawImage(image_path, 0, 0, img_width, img_height)
        c.showPage()

    # Save the PDF file
    c.save()


def get_png_images_from_directory(directory_path):
    # Get a list of all PNG files in the directory
    png_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.lower().endswith('.png')]
    return png_files


def convert_images_to_separate_pdfs(directory_path, output_directory):
    # Get all PNG images from the directory
    image_paths = get_png_images_from_directory(directory_path)

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for image_path in image_paths:
        # Create a unique output path for each PDF
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_pdf_path = os.path.join(output_directory, f"{base_name}.pdf")
        # Convert the image to a PDF
        image_to_pdf(image_path, output_pdf_path)


# Directory containing PNG images
input_directory = 'C:/Users/sms/Desktop/belgelerim'  # Replace with your directory path
# Directory where PDF files will be saved
output_directory = 'C:/Users/sms/Desktop/belgelerim/pdfs'  # Replace with your desired output directory

convert_images_to_separate_pdfs(input_directory, output_directory)
