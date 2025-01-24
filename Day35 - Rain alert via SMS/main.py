import requests
import os
from twilio.rest import Client


API_KEY_WEATHERAPP = os.environ.get("OWM_API_KEY")
MY_LAT = 52.520008 # Your latitude
MY_LONG = 13.404954 # Your longitude

account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")


#as per documentation, I can get the lat and lon one by using this: 
# "http://api.openweathermap.org/geo/1.0/direct?q=berlin}&limit=5}&appid=ac2420eb7085ab4b1831ca38ca6ea340"

#and now, we have the info, which aligns with our previous satelite work!
  #  "lat": 52.5170365,
 #   "lon": 13.3888599,
#    "country": "DE"

#We get the new API code form the documentation:
#https://api.openweathermap.org/data/2.5/weather?lat=52.5170365&lon=13.3888599&appid=ac2420eb7085ab4b1831ca38ca6ea340
#And we get our JSON!

#lets try for the 3 hour forecast one:
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY_WEATHERAPP,
    "units": "metric",
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
#print(response.status_code)
data = response.json()
#LOTS of data! so checking it in the https://jsonviewer.stack.hu/

#any way to itterate with a loog trough these middle keys/values? YES
will_rain = False
#Better witha  loop:
for hour_data in data['list']:
    code = hour_data['weather'][0]['id']
    #if id less than 700... use an umbrella!
    if int(code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its going to RAIN oh noooo...",
        from_="+16204558341",
        to="+491724589465",
    )


else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="No rain today no WOrrieeess...!",
        from_="+16204558341",
        to="+491724589465",
    )
    


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


"""client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+16204558341",
    to="+491724589465",
)

print(message.body)"""

