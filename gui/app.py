import tkinter as tk
from tkinter import ttk

class App:

    def __init__(self):
        self.window = None
        self.label = None
        self.label_content = None

    def start_application(self):
        # Tkinter-window
        self.window = tk.Tk()
        self.window.title("Alarmmonitor")
        self.window.attributes('-fullscreen', True)

        # Style for Treeview
        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 18))
        style.configure("Treeview.Heading", font=("Helvetica", 18))
        style.configure("Treeview", rowheight=40)

        # Erstellen Sie eine Treeview-Tabelle
        self.tree = ttk.Treeview(self.window, style="Treeview", height=25)
        self.tree["columns"] = ("value")
        self.tree.column("#0", minwidth=100, stretch=tk.NO)
        self.tree.column("value", minwidth=200)
        self.tree.heading("#0", text="Eigenschaft")
        self.tree.heading("value", text="Wert")

        self.tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Starten Sie die Tkinter-Hauptereignisschleife
        self.window.mainloop()

    def update_content(self, content: dict):
        # Löschen Sie die vorhandenen Einträge in der Tabelle
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fügen Sie die aktualisierten Inhalte zur Tabelle hinzu
        for key, value in content.items():
            self.tree.insert("", "end", text=key, values=(value,))

