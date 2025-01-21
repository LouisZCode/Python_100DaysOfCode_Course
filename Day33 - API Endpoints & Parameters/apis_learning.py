#not part of Python, to install when used!
import requests

#This will help us create a request from an url.
#This needs the Lodation of the API
response = requests.get(url='http://api.open-notify.org/iss-now.json')

print(response)  #this gives backa  response status code!   [200] which is successful!
#[404] is a bad one, Not Found!
#get more of the status code with
"""response.status_code"""

#But what if there are errors or problems and the code is not [200]?
#Then we can use the response.raide_for_status()
response.raise_for_status()

#now, how do we tap into the information inside our URL??
#easy, we get the JSON
data = response.json()
print(data)

#and as it is a dictionary, we can tap into its keys! lets try:
latitude = data['iss_position']["latitude"]
longitude = data['iss_position']['longitude']
print(f"lat is {latitude}, and lon is {longitude}")

response = requests.get(url='https://api.kanye.rest')
data = response.json()
print(data['quote'])
