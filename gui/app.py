from .map import Map
from mail_client.mail import KEYWORD_ADRESSE, extract_coordinates_from_content
import tkinter as tk
from tkinter import ttk
from tkinter import Button
from datetime import datetime
from logger import logger

class App:

    def __init__(self):
        self.window = None
        self.left_block = None # space for text
        self.right_block = None # space for map
        self.map = None
        self.line_widgets = []
        self.reset_button = None


    def start_application(self):
        # Tkinter-window
        self.window = tk.Tk()
        self.window.title('Alarmmonitor')
        self.window.attributes('-fullscreen', True)

        # configure column widths
        self.window.grid_columnconfigure(0, weight=1, uniform='column')
        self.window.grid_columnconfigure(1, weight=1, uniform='column')
        self.window.grid_rowconfigure(0, weight=1)

        self.left_block = ttk.Frame(self.window)
        self.left_block.grid(row=0, column=0, sticky='nesw')

        self.right_block = ttk.Frame(self.window)
        self.right_block.grid(row=0, column=1, sticky='nesw')

        # Configure the blocks to expand properly
        self.right_block.grid_rowconfigure(0, weight=1)
        self.right_block.grid_columnconfigure(0, weight=1)
        self.left_block.grid_columnconfigure(0, weight=1)

        self.map = Map(self.right_block)

        # Add button in the right buttom corner of the right_block
        self.reset_button = Button(self.right_block, text="reset")
        self.reset_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10) # 10 pixels padding from right and bottom
        self.reset_button.config(command=self.reset_view)


        self.window.mainloop()


    def update_content(self, content: dict):
        if(len(content) == 0):
            return
        
        self.reset_view()

        key_widgets = []
        value_widgets = []

        content, latitude, longitude = extract_coordinates_from_content(content)

        i = 0
        # Add new content to left_block
        for key, value in content.items():
            #create new Line for a key-value pair
            new_line_widget = ttk.Label(self.left_block)
            new_line_widget.grid(row=i, column=0, sticky='nesw') #nw
            self.line_widgets.append(new_line_widget)
            i += 1

            line_separator = tk.Canvas(self.left_block, height=2, bg='black', highlightthickness=0)
            line_separator.grid(row=i, column=0, sticky='nesw') #ew
            i += 1

            key_widget = ttk.Label(new_line_widget, text=key, background='grey', width=15, font=('Helvetica', 36, 'bold')) # width in characters (depending on font)
            value_widget = ttk.Label(new_line_widget, text=value, font=('Helvetica', 36, 'bold')) # no width -> expand in x direction because of side left
            
            key_widget.grid(row=0, column=0, sticky='nsw')
            value_widget.grid(row=0, column=1, sticky='nesw')

            key_widgets.append(key_widget)
            value_widgets.append(value_widget) # save all value labels for setting wraplength aferwards

        self.window.after(10, self._set_value_wraplengths(key_widgets, value_widgets))
        self.map.set_position(latitude, longitude, content[KEYWORD_ADRESSE])
        logger.info("Anzeigeinhalt aktualisiert")


    def reset_view(self):
        for widget in self.left_block.winfo_children():
            widget.destroy()
        self.map.reset_map()
        logger.info("Anzeige zurückgesetzt")


    def _set_value_wraplengths(self, key_widgets, value_widgets):
        self.left_block.update_idletasks()
        wrap_len = self.window.winfo_width() - self.right_block.winfo_width() - key_widgets[0].winfo_width()
        for label in value_widgets:
            label.configure(wraplength=wrap_len)
