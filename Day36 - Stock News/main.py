from news_call import get_headlines
from calculate_porcentaje import calculate_porcentage
#from stock_price import get_stock_price


STOCK = "TSLA"
COMPANY_NAME = "Tesla"
NEWS_API_KEY = '671121ad496547308763249441f565e9'
STOCK_INFO_API = "RAEJ1JDBDRNWQ7QR"
#Test at the end! this has a 25 uses limit per day


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#get_stock_price()   goes insite calculate porcentage

previous_num = 79
current_num = 81

if previous_num > current_num:
    print(f"{calculate_porcentage(previous_num , current_num)}% lose")
else:
    print(f"{calculate_porcentage(previous_num, current_num)}% profit")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
get_headlines(3)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

