import requests
from math import sin, cos, sqrt, atan2, radians
from modules.users import get_users
from modules.me import get_me
import sys


def get_coordinates():
    url = "https://hackathlon.nitorio.us/coordinates"
    response = requests.get(url).json()
    return response


def get_friend_coordinates():
    users = get_users()
    me = get_me()
    users_coordinates = get_coordinates()
    my_coordinates = get_user_coordinates(me['id'], users_coordinates, users)
    clean_coordinate_data = clear_coordinate_data(users_coordinates, users)
    distances = get_distance_list(clean_coordinate_data, my_coordinates[2], my_coordinates[3])
    return distances


def get_own_coords():
    users = get_users()
    me = get_me()
    users_coordinates = get_coordinates()
    return (str(get_user_coordinates(me['id'], users_coordinates, users)[2]) + "%2C" +
            str(get_user_coordinates(me['id'], users_coordinates, users)[3]))


def get_user_coordinates(id, users_coordinates, users):
    for user in users_coordinates:
        if user['userId'] == id:
            return id, get_user_name_by_id(id, users), user['coordinates']['lat'], user['coordinates']['long']
    return None


def get_user_name_by_id(id, users):
    for user in users:
        if user['id'] == id:
            return user['name']
    return "no name"


def clear_coordinate_data(user_coordinates, users):
    clean_coordinates = []
    for user in user_coordinates:
        clean_coordinates.append(get_user_coordinates(user['userId'],
                                                      user_coordinates,
                                                      users))
    return clean_coordinates


def get_distance_list(clean_coordinates_data, toLat, toLong):
    distances = []
    for user in clean_coordinates_data:
        dist = get_distance(toLat, toLong, user[2], user[3])
        distances.append((user[1], dist))

    return distances


def get_distance(lat1, lon1, lat2, lon2):
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return round(distance * 1000)
