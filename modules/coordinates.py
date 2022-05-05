import requests

def get_coordinates():
    url = "https://hackathlon.nitorio.us/coordinates"
    response = requests.get(url).json()
    return response
