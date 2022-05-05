import requests

def get_activities():
    try:
        url = "https://hackathlon.nitorio.us/activities"
        response = requests.get(url).json()
    except:
        "broke : D"
    return response