import pdfplumber

# Function to convert PDF to TXT
def pdf_to_txt(pdf_file, txt_file):
    with pdfplumber.open(pdf_file) as pdf:
        with open(txt_file, 'w', encoding='utf-8') as f:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    f.write(text)

# Usage
pdf_to_txt('Listato_revisioni_AB_2016_1ed_per_web.pdf', 'output_pandas.csv')
