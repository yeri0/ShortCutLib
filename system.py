from Shortcut import Shortcut
import sqlite3

def add_shortcut(shortcut: Shortcut):
    with sqlite3.connect("shortcuts.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shortcuts (name, description, shortcut_string) VALUES (?, ?, ?)", (shortcut.get_name(), shortcut.get_description(), shortcut.get_shortcut()))
        conn.commit()

def get_shortcuts():
    with sqlite3.connect("shortcuts.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shortcuts")
        return cursor.fetchall()

def delete_shortcut(shortcut):
    pass

def change_name(shortcut: Shortcut, new_name):
    pass

def change_description(shortcut: Shortcut, new_description):
    pass

def search(shortcut: Shortcut):
    pass
