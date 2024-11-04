import pdfplumber
import pandas as pd
import csv

# Function to convert PDF to TXT
def pdf_to_txt(pdf_file, txt_file):
    with pdfplumber.open(pdf_file) as pdf:
        with open(txt_file, 'w', encoding='utf-8') as f:
            for page_number in range(len(pdf.pages)):
                if page_number < 4:
                    continue
                
                page = pdf.pages[page_number]
                text = page.extract_text()
                
                if text:  # Check if there's text in the page
                    # Split text into lines
                    lines = text.splitlines()
                    for line in lines:
                        stripped_line = line.strip()
                        # Skip lines that contain only 'A', 'I', 'S', or 'D'
                        if (stripped_line in {'A', 'I', 'S', 'D'}) or (stripped_line and stripped_line[0].isdigit()):
                            continue
                        # Write the line to the text file
                        f.write(line + '\n')  # Add a newline for proper formatting

def combine_to_above():
    with open('output_SUP_2014_per_web.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        combined_lines = []
        previous_line = ""

        for row in csv_reader:
            # Join the row into a single string (in case there are multiple columns)
            current_line = ' '.join(row)

            # Check if the current line starts with 'V' or 'F'
            if current_line.startswith('V') or current_line.startswith('F') or current_line.startswith('N') or current_line.startswith('['):
                # If previous line exists, append it to the combined lines
                if previous_line:
                    combined_lines.append(previous_line)
                previous_line = current_line  # Set current line as previous for the next iteration
            else:
                # Combine the current line with the previous line
                previous_line += ' ' + current_line

        # Append the last processed line if it exists
        if previous_line:
            combined_lines.append(previous_line)

    # Output the combined lines
    with open('text/output_SUP_2014_per_web.csv', mode='w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)

        for line in combined_lines:
            # Write each combined line as a new row in the output file
            csv_writer.writerow([line])  # Write line as a single-element list

    # print("Output saved to 'combined_output.csv'.")

# pdf_to_txt('Listato_SUP_2014_per_web (2).pdf', 'output_SUP_2014_per_web.csv')

combine_to_above()
