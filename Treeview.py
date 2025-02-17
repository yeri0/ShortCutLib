from tkinter import ttk
from system import*

class tree:
    columns = ("Name", "Shortcut", "Beschreibung")

    def __init__(self, root_window, show, height):
        self.tree = ttk.Treeview(root_window, columns=self.columns, show=show, height=height)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Shortcut", text="Shortcut")
        self.tree.heading("Beschreibung", text="Beschreibung")
        self.tree.column("Name", width=80)
        self.tree.column("Shortcut", width=200)
        self.tree.column("Beschreibung", width=400)

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for shortcut in get_shortcuts():
            self.tree.insert("", "end", values=shortcut)
        
        print("Refreshing Table")