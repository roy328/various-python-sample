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
    image_R INT DEFAULT 0,
    image_G INT DEFAULT 0,
    image_B INT DEFAULT 0               
)
''')

# Step 3: Read data from CSV file and insert it into the database
with open('text/output_AM_2015.csv', mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    numero_num = ''
    
    for row in csvreader:
        correct = False
        if row['Signals'].startswith("Numero"):
            numero_num = row['Signals'].replace("Numero ministeriale: ", "")
            print(numero_num)
        else:
            if row['Signals'].startswith('V'):
                correct = True
            output_string = row['Signals'].split(") ", 1)[1].strip()

            cursor.execute('''
            SELECT COUNT(*) FROM traffic_signals 
            WHERE description = ? AND numero_ministeriale = ?
            ''', (output_string, numero_num))
            exists = cursor.fetchone()[0]

            # Insert only if it doesn't exist
            if exists == 0:
                cursor.execute('''
                INSERT INTO traffic_signals (numero_ministeriale, description, correct, pdf_type)
                VALUES (?, ?, ?, ?)
                ''', (numero_num, output_string, correct, "AM_2015"))
            else:
                print(f"'{output_string}' already exists. Skipping insertion.")
# Step 4: Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully!")
