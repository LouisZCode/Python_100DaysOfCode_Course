import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = 'https://api.sheety.co/ba7962d361651aea1732c73e02efb6c3/flightDeals/prices'

#This data managet class will create objects that interact with Sheety... meaning, I need this:
#Attibutes that hold all sheety info (urls, endpoints, passwords, etc...)
#Methods that use that info to Get, Put, or anything that can be done with Sheety.
#As it will be interacting with other APIs, to return all this info in a json format (or a readable format)

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data = {}
        
        
    def get_sheety_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
    
    def put_sheety_data(self, data):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                #auth=self._authorization
            )
        print(response.text)
