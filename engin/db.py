import csv
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('jarvis.db')
cursor = connection.cursor()


# connection.execute('DROP TABLE IF EXISTS contacts')
 
# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
#cursor.execute(query)
#connection.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# connection.commit()

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0,27]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
connection.commit()
connection.close()

# 4. Insert Single contacts (Optional)


#query = "INSERT INTO contacts VALUES (null,'satva', '6359212003',null)"
#cursor.execute(query)
#connection.commit()

# 5. Search Contacts from database
#query = 'ishu'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])