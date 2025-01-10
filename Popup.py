from tkinter import *
from tkinter import simpledialog
from databank import *

class Popup:
    def __init__(self, root):
        #Dialog Fenster initialisieren
        self.hinzufuegen_pop_up = Toplevel(root)
        self.hinzufuegen_pop_up.geometry("400x200")
        self.hinzufuegen_pop_up.title("Shortcut hinzufuegen")
        #Eingabefelder erstellen
        self.shortcut_entry = Entry(self.hinzufuegen_pop_up, bd=5, width=40)
        shortcut_label = Label(self.hinzufuegen_pop_up, text="Geben Sie Ihren Shortcut ein:")
        self.description_entry = Entry(self.hinzufuegen_pop_up, bd=5, width=40)
        description_label=Label(self.hinzufuegen_pop_up, text="Beschreiben Sie Ihr Shortcut:")

        #Submit button erstellen
        submit_button = Button(self.hinzufuegen_pop_up, text = "Erstellen", command = self.read_entry_data)

        #Elemente anzeigen:
        shortcut_label.pack()
        self.shortcut_entry.pack()
        description_label.pack()
        self.description_entry.pack()
        submit_button.pack()
        print("The Popup has been created")
    
    def read_entry_data(self):
        print("read_entry_data")
        shortcut = self.shortcut_entry.get()
        description = self.description_entry.get()
        add_shortcut(Shortcut("",shortcut,description,))
        self.hinzufuegen_pop_up.destroy()