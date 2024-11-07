import csv
import sqlite3

# Step 1: Connect to SQLite database (it will create one if it doesn't exist)
connection = sqlite3.connect('signals.db')
cursor = connection.cursor()

# Step 2: Create a table for the traffic signals
cursor.execute('''
CREATE TABLE IF NOT EXISTS traffic_signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_ministeriale TEXT,
    description TEXT,
    correct BOOLEAN,
    pdf_type TEXT,
    image_path TEXT,
    image_R INT DEFAULT 0,
    image_G INT DEFAULT 0,
    image_B INT DEFAULT 0               
)
''')

# Step 3: Read data from CSV file and insert it into the database
with open('quizzes.csv', mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    numero_num = ''
    
    next(csvreader, None)
    
    # Store the data in a list
    data = []
    for row in csvreader:
        data.append(row)
    
    # Example: Print all questions and their answers
    for question, answer in data:
        # print(f"Question: {question}, Answer: {answer}")

        cursor.execute('''
        SELECT COUNT(*) FROM traffic_signals 
        WHERE description = ? 
        ''', (question,))
        exists = cursor.fetchone()[0]
        correct = True if answer == 'V' else False
        # Insert only if it doesn't exist"
        if exists == 0:
            cursor.execute('''
            INSERT INTO traffic_signals (numero_ministeriale, description, correct, pdf_type)
            VALUES (?, ?, ?, ?)
            ''', (numero_num, question, correct, "Online_Quiz"))
        else:
            print(f"'{question}' already exists. Skipping insertion.")
# Step 4: Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully!")
