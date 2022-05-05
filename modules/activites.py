import requests

def get_activities():
    url = "https://hackathlon.nitorio.us/activites"
    response = requests.get(url).json()
    return response