import requests

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_INFO_API = "RAEJ1JDBDRNWQ7QR"
STOCK = "PLTR"

def get_stock_price(day1, day2):

    stock_api_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': STOCK_INFO_API,
        'outputsize': 'compact',
        }

    #Stock API Docs: https://www.alphavantage.co/documentation/
    #https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=PLTR&outputsize=compact&apikey=RAEJ1JDBDRNWQ7QR

    response = requests.get(url='https://www.alphavantage.co/query?', params=stock_api_params)
    stock_data = response.json()
    #print(stock_data)


    #Now lets tap into yestedays and day before price data:
    recent_price = (stock_data['Time Series (Daily)'][str(day1)]['4. close'])
    previous_price = (stock_data['Time Series (Daily)'][str(day2)]['4. close'])

    return recent_price, previous_price

#prices = get_stock_price('2025-01-24', '2025-01-23')
#print(prices)
