#impport nominatim api
from geopy.geocoders import Nominatim

#activate nominatim geocoder
locator = Nominatim(user_agent="myGeocoder")
#type any address text
location = locator.geocode("Green Park, Kanpur")

#print latitude and longitude of the address
#print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

#the API has multiple other details as a json like altitude, latitide,longitude, correct raw address, etc
#print(location.raw,location.point,location.latitude, location.longitude,location.altitude,location.address)

#trying nother address
location2 = locator.geocode("Z Square, Kanpur")

#the API has multiple other details as a json like altitude, latitide,longitude, correct raw address, etc
print(location2.raw,location2.point,location2.latitude, location2.longitude,location2.altitude,location2.address)