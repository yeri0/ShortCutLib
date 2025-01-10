from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from system import *
import Popup
from databank import clear_data_bank

#Funktion soll ein Dialogfenster öffnen, dass dann mit den nötigen Infos einen neuen Shortcut zur Lib hinzufügt
def add_button_action():
    print("add_button_action was clicked")
    popup = Popup.Popup(fenster)
    


#Funktion soll Dialogfenster öffnen, dass bestimmten Shortcut wieder entfernt
def delete_button_action():
    print("delete_button_action was pressed")

# Ein Fenster erstellen
fenster = Tk()
#Geometrie einstellen
fenster.geometry("750x480")
# Den Fenstertitel erstellen
fenster.title("ShortCutLib")

#Buttons erstellen
add_button = Button(fenster, text="Hinzufügen", command = add_button_action)
delete_button = Button(fenster, text="Entfernen", command = delete_button_action)
clear_database_button = Button(fenster, text="Datenbank leeren", command = clear_data_bank)

#Button zum Fenster hinzufügen
add_button.grid(row = 0, column = 0, sticky="e", padx=5, pady=5)
delete_button.grid(row = 0, column = 1, sticky="e", padx=5, pady=5)
clear_database_button.grid(row = 0, column = 2, sticky="ne", padx=5, pady=5)

#In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()