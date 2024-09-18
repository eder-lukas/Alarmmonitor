from tkinter import ttk
import tkintermapview
from geopy.geocoders import Nominatim
import re

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
        self.reset_map()


    def set_position(self, latitude, longitude, address):
        if latitude and longitude:
            self._set_position_by_coordinates(latitude, longitude)
        else:
            self._set_position_by_address(address)


    def _set_position_by_coordinates(self, latitude, longitude):
        if self.map_widget:
            try:
                latitude=float(latitude)
                longitude=float(longitude)
            except:
                print("Koordinaten konnten nicht von String zu Float konvertiert werden. Latitude: " + str(latitude) + "; Longitude: " + str(longitude))

            if isinstance(latitude, float) and isinstance(longitude, float):
                self.map_widget.set_position(latitude, longitude)
                self._set_marker(latitude, longitude)


    def _set_position_by_address(self, address):
        if address:
            location = None
            try:
                location = self.geolocator.geocode(address)
            except:
                pass
            if not(location):
                address_without_city_name = self._remove_city_name_from_address(address)
                try:
                    location = self.geolocator.geocode(address_without_city_name)
                except:
                    pass
            if location:
                self._set_position_by_coordinates(location.latitude, location.longitude)
                self._set_marker(location.latitude, location.longitude)
            else:
                print(f"Address '{address}' could not be geocoded.")


    def _remove_city_name_from_address(self, address) -> str:
        last_number = re.search(r'\d(?!.*\d)', address)
        if last_number:
            return address[:last_number.end()]
        return address # if there is no number (zip code) inside the string


    def _set_marker(self, latitude, longitude):
        if self.map_widget:
            self.map_widget.set_marker(latitude, longitude)
            

    def reset_map(self):
        self._set_position_by_coordinates(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)
        self.map_widget.delete_all_marker()
        
