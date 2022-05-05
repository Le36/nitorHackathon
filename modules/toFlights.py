import requests


def get_toFlights():
    url = "https://hackathlon.nitorio.us/toFlights"
    response = requests.get(url).json()
    return response
