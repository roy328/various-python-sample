import sqlite3

# Connect to the SQLite database (ensure you have the correct path)
connection = sqlite3.connect('signals.db')  # Change to your database path
cursor = connection.cursor()

# Fetch all rows in the table
cursor.execute("SELECT id, description FROM traffic_signals")  # Assuming there's an 'id' column for primary key
rows = cursor.fetchall()

def clean_string(input_string):
    return (input_string
            .replace("() ", "")
            .replace('  ', ' ')
            .replace('- ', '')
            .replace('-', '')
            .replace('.', '')
            .replace(', ', ',')
            .replace("’i", '')
            .replace("'i", "")
            .replace("‘i", "")
            .replace("E ", 'E')
            .replace("È", 'E')
            .replace("’ ", '')
            .replace("’", '')
            .replace("' ", "")
            .replace("'", "")
            .replace("‘ ", "")
            .replace("‘", "")
            .replace('“', '"')
            .replace('N', 'V')
            .replace('K', 'k')
            .replace('i', 'l')
            .replace('î', 'l')
            .replace('f', 'l')
            .replace('1', 'l')
            .replace('I', 'l')
            .replace('[', 'l')
            .replace(']', 'l')
            .replace('{', 'l')
            .replace('(', 'l')
            .replace('}', 'l')
            .replace(')', 'l')
            .replace('!', 'l')
            .replace('|', 'l')
            .replace('U', 'l')
            .replace('L', 'l')
            .replace('é', 'e')
            .replace('è', 'e')
            .replace('j', 'o')
            .replace('à', 'o')
            .replace('a', 'o')
            .replace('ù', 'o')
            .replace('&', 'o')
            .replace('€', 'o')
            .replace('d', 'o')
            .replace('ò', 'o')
            .replace('0', 'o')
            .replace('rl', 'n')
            .replace('nl', 'n')
            .replace('ul', 'u')
            .replace('5 t', '5t')
            .replace('T e', 'Te')
            .replace('D e', 'De')
            .replace('o l', 'ol')
            .replace('l s', 'ls')
            .replace('l v', 'lv')
            .replace('l m', 'm')
            .replace('ll', 'l')
            .replace(' } ', ' '))

for row in rows:
    id_value = row[0]  # Assuming first element is the id
    question = row[1]
    
    # Clean the question string
    cleaned_question = clean_string(question)
    
    # Update the question in the database
    cursor.execute("UPDATE traffic_signals SET description = ? WHERE id = ?", (cleaned_question, id_value))

# Commit the changes
connection.commit()

print("success")
