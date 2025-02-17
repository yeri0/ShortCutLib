import sqlite3

# Connect to SQLite (creates the file if it doesnt´t exitst)
conn = sqlite3.connect("shortcuts.db")
cursor = conn.cursor()

#Create a table for shortcuts
cursor.execute('''CREATE TABLE IF NOT EXISTS shortcuts(
               name TEXT PRIMARY KEY NOT NULL,
               description TEXT NOT NULL,
               shortcut_string TEXT NOT NULL)''')

#save and close
conn.commit()
conn.close()