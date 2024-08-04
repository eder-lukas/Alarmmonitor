from tkinter import ttk
import tkintermapview
from geopy.geocoders import Nominatim

DEFAULT_LATITUDE=48.688687
DEFAULT_LONGITUDE=11.109092

class Map:
    def __init__(self, parent_widget: ttk.Frame) -> None:
        self.parent_widget = parent_widget
        self.map_widget = None
        self.geolocator = Nominatim(user_agent="Alarmmonitor")
        self._insert_map()


    def _insert_map(self):
        self.map_widget = tkintermapview.TkinterMapView(self.parent_widget)
        self.map_widget.grid(row=0, column=0, sticky='nesw')
        self.set_position(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)


    def set_position(self, latitude, longitude):
        if self.map_widget:
            self.map_widget.set_position(latitude, longitude)


    def set_position_by_address(self, address, address_without_city):
        if address:
            location = None
            try:
                location = self.geolocator.geocode(address)
            except:
                pass

            if not location:
                try:
                    location = self.geolocator.geocode(address_without_city)
                except:
                    pass

            if location:
                self.set_position(location.latitude, location.longitude)
                self._set_marker(location.latitude, location.longitude)
            else:
                print(f"Address '{address}' could not be geocoded.")


    def _set_marker(self, latitude, longitude):
        if self.map_widget:
            self.map_widget.set_marker(latitude, longitude)
            

    def reset_map(self):
        self.map_widget.delete_all_marker()
        self.set_position(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)
        
