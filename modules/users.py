import requests

def get_users():
    url = "https://hackathlon.nitorio.us/users"
    response = requests.get(url).json()
    return response

def get_user(user_id):
    url = "https://hackathlon.nitorio.us/users"
    users = requests.get(url).json()
    