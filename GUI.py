from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from system import *
import Popup
import Treeview


#Funktion soll ein Dialogfenster öffnen, dass dann mit den nötigen Infos einen neuen Shortcut zur Lib hinzufügt
def add_button_action():
    print("add_button_action was clicked")
    popup = Popup.Popup(fenster, tree)

#Funktion soll Dialogfenster öffnen, dass bestimmten Shortcut wieder entfernt
def delete_button_action():
    print("delete_button_action was pressed")

# Create the main window
fenster = Tk()
fenster.geometry("750x480")
fenster.title("ShortCutLib")

tree = Treeview.tree(fenster,show="headings", height=20)

# Buttons
add_button = Button(fenster, text="Hinzufügen", command=add_button_action)
delete_button = Button(fenster, text="Entfernen", command=delete_button_action)

# Load to window
add_button.grid(row=0, column=0, sticky="e", padx=5, pady=5)
delete_button.grid(row=0, column=1, sticky="e", padx=5, pady=5)
tree.tree.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


# Load existing shortcuts into the table
fenster.after(0, tree.refresh_table)

# Start the Tkinter event loop
fenster.mainloop()