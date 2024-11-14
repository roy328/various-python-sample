import csv

# Paths to your files
text_file_path = 'tutte.txt'  # Path to the text file
csv_file_path = 'quizzes.csv'      # Path to the existing CSV file

# Step 1: Read the text file line by line
with open(text_file_path, 'r', encoding='utf-8') as txt_file:
    lines_to_add = txt_file.readlines()

# Step 2: Clean lines and compare (remove newline characters)
cleaned_lines = [line.strip() for line in lines_to_add]

new_lines = []
amount = 1

# Step 3: Read existing CSV and store questions in a set for quick lookup
existing_questions = set()

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csvreader = csv.reader(file)
    
    # Populate the set with existing questions
    for row in csvreader:
        if row:  # Check if the row is not empty
            existing_questions.add(row[0])  # Assuming the question is in the first column

# Step 4: Process cleaned lines from the text file
for i, line in enumerate(cleaned_lines, start=1):
    parts = line.split(';')
    
    # Ensure parts exist
    if len(parts) < 3:
        continue

    question = parts[1].strip()

    # Determine the answer based on the third part
    answer = "V" if parts[2] == "VERO" else "F"

    # Check if the question already exists
    if question not in existing_questions:
        new_lines.append([question, answer])
        print(amount, "string inserted")
        amount+=1

# Step 5: Append new lines to the CSV if there are any new questions
if new_lines:
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(new_lines)

    print(f"Successfully added {len(new_lines)} new lines to the CSV.")
else:
    print("No new lines were added. All lines are duplicates.")

