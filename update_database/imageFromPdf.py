import PyPDF2
import os

def extract_images(pdf_file, out_folder):
    # Create a directory for extracted images
    os.makedirs('extracted_images', exist_ok=True)

    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_number, page in enumerate(reader.pages):
            if '/XObject' in page['/Resources']:
                xObject = page['/Resources']['/XObject'].get_object()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        image_data = xObject[obj]._data
                        image_extension = xObject[obj]['/Filter'][0][1:]  # Get extension from filters
                        image_extension = image_extension.decode("utf-8")
                        image_file_path = os.path.join('extracted_images', f'image_page_{page_number + 1}_{obj[1:]}.{image_extension}')
                        
                        with open(image_file_path, 'wb') as img_file:
                            img_file.write(image_data)

pdf_path = 'Listato_revisioni_AM_2016_1ed_per_web.pdf'  # Path to your PDF file
output_folder = 'extracted_images'  # Folder to save the extracted images

extract_images(pdf_path, output_folder)
