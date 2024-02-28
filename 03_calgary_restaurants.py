import requests
from pprint import pprint
from getpass import getpass

#api_key = getpass("Enter your Google Maps API key: ")
api_key = "AIzaSyDi-Rmx_PZdXDfca7jr3jNTS_bxauDfu1Q"
location = "Calgary"

# Google Maps API for geocoding
geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
response = requests.get(
    geocode_url,
    params={
        'address': location,
        'key': api_key
    }
)
geocode_data = response.json()
# pprint(geocode_data)
latitute = geocode_data['results'][0]['geometry']['location']['lat']
longitude = geocode_data['results'][0]['geometry']['location']['lng']

# Google Maps API for nearby restaurants
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

response = requests.get(
    url,
    params={
        'location': f"{latitute},{longitude}",
        'radius': 1500,
        'type': 'restaurant',
        'key': api_key
    }
)
data = response.json()

restaurants = []
for place in data['results']:
    restaurant = {
        'name': place['name'],
        'rating': place.get('rating', 'N/A'),
        'address': place.get('vicinity', 'N/A'),
    }
    restaurants.append(restaurant)

for restaurant in restaurants:
    print(f"{restaurant['name']} - {restaurant['address']} - {restaurant['rating']}")
