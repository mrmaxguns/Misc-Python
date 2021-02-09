"""
Scrape weather data from MetaWeather.com.
"""

import requests
from typing import Optional
from datetime import datetime
import urllib.parse


def query_locations_by_name(location_name: str) -> list:
    """Returns a list of locations matching the location name"""
    payload = {"query": location_name}
    request = requests.get(
        "https://www.metaweather.com/api/location/search/",
        params=payload
    )
    return _parse(request)


def query_locations_by_lat_long(lattitude: float, longitude: float) -> list:
    """Returns a list of locations near the lattitude and longitude specified"""
    query = [str(lattitude), str(longitude)]
    payload = {"lattlong": ",".join(query)}
    request = requests.get(
        "https://www.metaweather.com/api/location/search/",
        params=payload
    )
    return _parse(request)


def get_weather(woeid: int, date: Optional[datetime] = None) -> dict:
    """Gets the weather of a location based on the woeid (where on earth id)"""
    woeid = str(woeid) + "/"
    if date is None:
        url = urllib.parse.urljoin(
            "https://www.metaweather.com/api/location/",
            woeid
        )
    else:
        url = urllib.parse.urljoin(
            urllib.parse.urljoin(
                "https://www.metaweather.com/api/location/",
                woeid
            ),
            date.strftime("%Y/%m/%d/")
        )

    request = requests.get(url)
    return _parse(request)


def get_weather_by_name(
    location_name: str,
    date: Optional[datetime] = None
) -> dict:
    """Gets the weather of a location by the location's name"""
    locations = query_locations_by_name(location_name)
    if not locations:
        raise Exception("location not found")
    woeid = locations[0]["woeid"]
    return get_weather(woeid, date)


def _parse(request):
    """Parse a request; make sure the status code is 200, and return the JSON"""
    if request.status_code != 200:
        raise Exception(
            f"could not retrieve data with status code {request.status_code}"
        )
    return request.json()
