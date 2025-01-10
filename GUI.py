from tkinter import *
import tkinter as tk
from tkinter import simpledialog

def read_entry_data(shortcut_entry, describtion_entry):
    shortcut = shortcut_entry.get()
    describtion = describtion_entry.get()
    print(shortcut)
    print(describtion)

#Funktion soll ein Dialogfenster öffnen, dass dann mit den nötigen Infos einen neuen Shortcut zur Lib hinzufügt
def add_button_action():
    print("add_button_action was clicked")

    #Dialog Fenster initialisieren
    hinzufuegen_pop_up = Toplevel(fenster)
    hinzufuegen_pop_up.geometry("400x200")
    hinzufuegen_pop_up.title("Shortcut hinzufuegen")

    #Eingabefelder erstellen
    shortcut_entry = Entry(hinzufuegen_pop_up, bd=5, width=40)
    shortcut_label = Label(hinzufuegen_pop_up, text="Geben Sie Ihren Shortcut ein:")
    describtion_entry = Entry(hinzufuegen_pop_up, bd=5, width=40)
    describtion_label=Label(hinzufuegen_pop_up, text="Beschreiben Sie Ihr Shortcut:")

    #Submit button erstellen
    submit_button = Button(hinzufuegen_pop_up, text = "Erstellen", command = read_entry_data(shortcut_entry, describtion_entry))

    #Elemente anzeigen:
    shortcut_label.pack()
    shortcut.pack()
    describtion_label.pack()
    describtion.pack()


#Funktion soll Dialogfenster öffnen, dass bestimmten Shortcut wieder entfernt
def delete_button_action():
    print("delete_button_action was pressed")

# Ein Fenster erstellen
fenster = Tk()
#Geometrie einstellen
fenster.geometry("750x480")
# Den Fenstertitel erstellen
fenster.title("ShortCutLib")

#Add Button erstellen
add_button = Button(fenster, text="Hinzufügen", command = add_button_action)
delete_button = Button(fenster, text="Entfernen", command = delete_button_action)

#Button zum Fenster hinzufügen
add_button.grid(row = 0, column = 0, sticky="e", padx=5, pady=5)
delete_button.grid(row = 0, column = 1, sticky="e", padx=5, pady=5)

#In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()