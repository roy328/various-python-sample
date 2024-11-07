import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder='page_images'):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF document
    pdf_document = fitz.open(pdf_path)
    image_count = 0

    # Iterate through each page of the PDF
    for page_number in range(len(pdf_document)):
        if page_number < 4:
            continue
        page = pdf_document[page_number]
        
        # Render the page to a pixmap (image)
        pix = page.get_pixmap()

        # Save the pixmap as an image file
        image_name = f'page_{page_number - 3}.png'  # You can change the format if needed
        image_path = os.path.join(output_folder, image_name)
        pix.save(image_path)

        print(f'Saved full page screenshot: {image_path}')

    pdf_document.close()

# Example usage
pdf_path = 'Listato_KB_3ed_2019.pdf'  # Replace with your PDF file path
extract_images_from_pdf(pdf_path)
