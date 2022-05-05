import requests

def get_users():
    url = "https://hackathlon.nitorio.us/users"
    response = requests.get(url).json()
    return response
