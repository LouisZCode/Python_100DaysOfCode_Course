import requests
from datetime import datetime as dt

USERNAME = 'luiszg90'
TOKEN = 'luiszg90'
GRAPH_ID = 'codegraph01'

#Lets follow the information at the webpage https://pixe.la/  in the section HOW TO...

pixela_endpoint = 'https://pixe.la/v1/users'

#There is also a lot of get, puts and deletes in the documentation here: https://docs.pixe.la/
#So lets create an user!
#We get the parameters key for the Request Body in that same documentation
#USER CREATION

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

""" This was successfull, so lets comment it
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text) """

#'GRAPH CREATION'

graph_donfig = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'pomodoro',
    'type': 'int',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN,
}


""" This was successfull, so lets comment it
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
response = requests.post(url=graph_endpoint, json=graph_donfig, headers=headers)
print(response.text) """

# now you can check out your graphe here:  https://pixe.la/v1/users/luiszg90/graphs/codegraph01
#f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}'


#PIXEL CREATION
pixel_params = {
    'date': '20250129',
    'quantity':  '4',
}

""" This was successfull, so lets comment it
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text) """


#How do we automatically change the date to the format that we desire?
today = dt.now()
#print(today)

#we use the strftime method to put any format! (%Y, %m, %d)
DAY_FORMAT = today.strftime('%Y%m%d')
print(DAY_FORMAT)

#'Alternative:
#today_alt = dt.now(year=2020, month=1, day=29)
#print(today_alt)


update_pixel_params = {
    'quantity': '10',
}


""" This was successfull, so lets comment it
update_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DAY_FORMAT}'
response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
print(response.text) """

#'to delete it is basically the same endpoint!'