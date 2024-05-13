import tkinter as tk

class App:

    def __init__(self):
        self.window = None
        self.label = None

    def start_application(self, content: str):
        # Erstellen Sie ein Tkinter-Fenster
        self.window = tk.Tk()
        self.window.title("Alarmmonitor")
        self.window.attributes('-fullscreen', True)

        # Erstellen Sie ein Label, um den Text anzuzeigen
        self.label = tk.Label(self.window, text=content, font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Starten Sie die Tkinter-Hauptereignisschleife
        self.window.mainloop()

    def update_content(self, content: str):
        self.label.config(text=content)


# https://stackoverflow.com/questions/67112082/updating-text-after-running-mainloop-in-tkinter