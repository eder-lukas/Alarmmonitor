import tkinter as tk
from tkinter import ttk

DEFAULT_CONTENT = "Alarmmonitor-Anzeigetext"

class App:

    def __init__(self):
        self.window = None
        self.label = None
        self.label_content = None

    def start_application(self):
        # Erstellen Sie ein Tkinter-Fenster
        self.window = tk.Tk()
        self.window.title("Alarmmonitor")
        self.window.attributes('-fullscreen', True)

        # Erstellen Sie ein Label, um den Text anzuzeigen
        self.label_content = tk.StringVar()
        self.label_content.set(DEFAULT_CONTENT)
        self.label = ttk.Label(self.window, textvar=self.label_content, font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Starten Sie die Tkinter-Hauptereignisschleife
        self.window.mainloop()

    def update_content(self, content: str):
        self.label_content.set(content)


# https://stackoverflow.com/questions/67112082/updating-text-after-running-mainloop-in-tkinter