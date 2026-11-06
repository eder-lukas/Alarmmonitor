from load_env import load_default_latitude, load_default_longitude, load_mail
from tkinter import ttk
import tkintermapview
import tkintermapview.map_widget
import tkintermapview.offline_loading
import requests
from geopy.geocoders import Nominatim
import re
from logger import logger

DEFAULT_LATITUDE=load_default_latitude()
DEFAULT_LONGITUDE=load_default_longitude()

def _build_osm_user_agent() -> str:
    contact = load_mail()
    user_agent = "Alarmmonitor/1.0"
    if contact:
        user_agent += f" (contact: {contact})"
    return user_agent

OSM_USER_AGENT = _build_osm_user_agent()

class _UserAgentRequests:
    def __init__(self, requests_module, user_agent: str) -> None:
        self._requests = requests_module
        self._user_agent = user_agent

    def get(self, url, **kwargs):
        headers = dict(kwargs.pop("headers", None) or {})
        headers["User-Agent"] = self._user_agent
        return self._requests.get(url, headers=headers, **kwargs)

    def __getattr__(self, name):
        return getattr(self._requests, name)

def _patch_tkintermapview_user_agent() -> None:
    requests_with_user_agent = _UserAgentRequests(requests, OSM_USER_AGENT)
    tkintermapview.map_widget.requests = requests_with_user_agent
    tkintermapview.offline_loading.requests = requests_with_user_agent

_patch_tkintermapview_user_agent()

class Map:
    def __init__(self, parent_widget: ttk.Frame) -> None:
        self.parent_widget = parent_widget
        self.map_widget = None
        self.geolocator = Nominatim(user_agent=OSM_USER_AGENT)
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
                logger.error("Koordinaten konnten nicht von String zu Float konvertiert werden. Latitude: " + str(latitude) + "; Longitude: " + str(longitude))

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
                logger.warning(f"Address '{address}' could not be geocoded.")


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
        
