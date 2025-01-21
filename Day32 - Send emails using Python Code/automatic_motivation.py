#TODO-1 Tap into the quotes and make a list
#TODO-1.5 Create a email that will be sent
#TODO-2 Select a random quote and put it in the email
#TODO-3 if the X day is True, send the email

import random
import smtplib
import datetime as dt

MY_EMAIL = "luis.python.test1@gmail.com"
MY_PASS = "pspw dyul oigd ciua"

#1, tap into the qoutes database, make a list of it:
with open("quotes.txt", "r") as quotes:
    quote_list = list(quotes)
    #print(quote_list)

#2 select a random quote:
r_quote = quote_list[random.randint(0,len(quote_list))]   #could use the random.choice method, but all ok
#print(r_quote)

#acces the email
with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASS)
    #chech if the day is the day you want to send the email

    now = dt.datetime.now()
    print(now.weekday())

    if now.weekday() == 4:
        print("today, the email will be sent!")

        #now, just send the email
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="luis.python.test1@outlook.com",
                            msg=f"Subject:Quote of the day\n\nStop and reflect:\n{r_quote}")
    else:
        print("Email was not sent")


#Q, how do  activate this code to run while I am not here to click "GO"