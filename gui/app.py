import tkinter as tk
from tkinter import ttk

# DEFAULT_CONTENT = "Alarmmonitor-Anzeigetext"

class App:

    def __init__(self):
        self.window = None
        self.label = None
        self.label_content = None

    # def start_application(self):
    #     # Erstellen Sie ein Tkinter-Fenster
    #     self.window = tk.Tk()
    #     self.window.title("Alarmmonitor")
    #     self.window.attributes('-fullscreen', True)

    #     # Erstellen Sie ein Label, um den Text anzuzeigen
    #     self.label_content = tk.StringVar()
    #     self.label_content.set(DEFAULT_CONTENT)
    #     self.label = ttk.Label(self.window, textvar=self.label_content, font=("Helvetica", 14))
    #     self.label.pack(pady=20)

    #     # Starten Sie die Tkinter-Hauptereignisschleife
    #     self.window.mainloop()

    # def update_content(self, content: str):
    #     self.label_content.set(content)

    def start_application(self):
        # Erstellen Sie ein Tkinter-Fenster
        self.window = tk.Tk()
        self.window.title("Alarmmonitor")
        self.window.attributes('-fullscreen', True)

        # Erstellen Sie eine Treeview-Tabelle
        self.tree = ttk.Treeview(self.window)
        self.tree["columns"] = ("value")
        self.tree.column("#0", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column("value", width=200, minwidth=200, stretch=tk.NO)
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
            self.tree.insert("", "end", text=key, values=(value))
            