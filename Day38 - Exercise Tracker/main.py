import requests
from datetime import datetime as dt
import os



#NOTE NUTRITION API
NUTRITION_APP_ID = os.environ.get('NUTRITION_APP_ID')
NUTRITION_APP_KEYS = os.environ.get('NUTRITION_APP_KEYS')

exercise = input('What exercise did you do?')

exercise_params = {
    'query': exercise,
    'weight_kg': 80,
    'height_cm': 175,
    'age': 34,
}

headers = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITION_APP_ID,
    'x-app-key': NUTRITION_APP_KEYS,
  }

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response_exercise = requests.post(exercise_endpoint, json=exercise_params, headers=headers)
print(response_exercise.json())
duration = response_exercise.json()['exercises'][0]['duration_min']
calories = response_exercise.json()['exercises'][0]['nf_calories']



#NOTE SHEETY API
sheety_url = os.environ.get('SHEETY_URL')

response_sheety = requests.get(sheety_url)
#print(response)

today = dt.now()
date = today.strftime('%d.%m.%Y')
time = today.strftime('%H:%M')



alldata_json = {
  'workout' : {
      'date': date,
      'time': time,
      'exercise': exercise.title(),
      'duration': duration,
      'calories': calories,
  }
}


BEARER = os.environ.get('BEARER')
headers = {'Authorization' : BEARER}

add_row = requests.post(sheety_url, json=alldata_json, headers=headers)
print(add_row.text)


#Last step, secure the Environment Variables!!