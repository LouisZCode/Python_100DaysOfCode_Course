import requests
import datetime

BER_LAT = 52.520008
BER_LNG = 13.404954

#so, this one needs Parameters, how do we add them to the request?
#We can do dictionary with this perameters as Keys!
berlin_parameters = {
    "lat": BER_LAT,
    "lng": BER_LNG,
    "formatted": 0,
}
#I used Berlins Latitude and Longitude

today = datetime.datetime.now()
print(today.hour)

response = requests.get(url='https://api.sunrise-sunset.org/json', params=berlin_parameters)
response.raise_for_status()
data = response.json()
#print(data)
print(data["results"]["sunrise"].split("T")[1].split(":")[0])
print(data["results"]["sunset"].split("T")[1].split(":")[0])

#Another way to add this info, is in the url directly, like this: https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400