import requests


def get_me():
    url = "https://hackathlon.nitorio.us/me"
    response = requests.get(url).json()
    return response
