from tkinter import *
from tkinter import simpledialog
from system import *

class Popup:
    def __init__(self, root, tree):

        #Dialog Fenster initialisieren
        hinzufuegen_pop_up = Toplevel(root)
        hinzufuegen_pop_up.geometry("400x200")
        hinzufuegen_pop_up.title("Shortcut hinzufuegen")
        self.tree = tree

        #Eingabefelder erstellen
        self.name_entry = Entry(hinzufuegen_pop_up, bd=5, width=40)
        name_label = Label(hinzufuegen_pop_up, text="Vergeben Sie einen Namen")

        self.description_entry = Entry(hinzufuegen_pop_up, bd=5, width=40)
        description_label=Label(hinzufuegen_pop_up, text="Beschreiben Sie Ihr Shortcut:")

        self.shortcut_entry = Entry(hinzufuegen_pop_up, bd=5, width=40)
        shortcut_label = Label(hinzufuegen_pop_up, text="Geben Sie Ihren Shortcut ein:")

        self.description_entry = Entry(hinzufuegen_pop_up, bd=5, width=40)
        description_label=Label(hinzufuegen_pop_up, text="Beschreiben Sie Ihr Shortcut:")

        #Submit button erstellen
        submit_button = Button(hinzufuegen_pop_up, text = "Erstellen", command = self.read_entry_data)

        #Elemente anzeigen:
        name_label.pack()
        self.name_entry.pack()
        shortcut_label.pack()
        self.shortcut_entry.pack()
        description_label.pack()
        self.description_entry.pack()
        submit_button.pack()
        print("The Popup has been created")
    
    def read_entry_data(self):
        print("read_entry_data")
        name = self.name_entry.get()
        shortcut = self.shortcut_entry.get()
        description = self.description_entry.get()
        #Before Adding the Shortcut, check if the ID already exists
        add_shortcut(Shortcut(name,shortcut,description,))
        self.tree.refresh_table()
        self.shortcut_entry.winfo_toplevel().destroy()