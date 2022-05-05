import requests


def get_closest(current_coords):
    url = "https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%28nwr%5B%22amenity" \
          "%22%3D%22restaurant%22%5D%28around%3A2000%2C" + current_coords + \
          "%29%3B%29%20-%3E%20.results%3B%0A.results%20out%20center%3B "
    response = requests.get(url).json()
    return response["elements"]
