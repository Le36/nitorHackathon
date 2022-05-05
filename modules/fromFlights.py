import requests


def get_fromFlights():
    url = "https://hackathlon.nitorio.us/fromFlights"
    response = requests.get(url).json()
    return response
