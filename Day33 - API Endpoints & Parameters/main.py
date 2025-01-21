import requests
from datetime import datetime
import smtplib
import time

my_email = "luis.python.test1@gmail.com"
my_password = "pspw dyul oigd ciua"

#Lets use Berlin lat&long
MY_LAT = 52.520008 # Your latitude
MY_LONG = 13.404954 # Your longitude


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#print(sunset)

time_now = datetime.now()

while True:
    time.sleep(5)
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if int(iss_latitude) in range(48, 56) and int(iss_longitude) in range(7, 18):
        print("its in the area!")
        if time_now.hour > sunset:
            print("it is visible!")
            with smtplib.SMTP("smtp.gmail.com", port=25) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs="lgzg90@hotmail.com",
                                    msg="Subject:Greetings\n\nThe ISS is above you and it is visible!\n"
                                        f"latitude: {iss_latitude}, longitude: {iss_longitude}")


    else:
        print(iss_latitude, iss_longitude)
        print("it is NOT around!")





