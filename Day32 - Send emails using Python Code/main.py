##################### Extra Hard Starting Project ######################
import os
import random
import smtplib
import datetime as dt
import pandas

MY_EMAIL = "luis.python.test1@gmail.com"
MY_PASS = "pspw dyul oigd ciua"


#get a hold of todays day:
now = dt.datetime.now()
day = now.day
month = now.month
#print(day,month)

# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv", 'r') as birthdays:
    data = pandas.read_csv(birthdays)
    #print(data.columns)
    for (index, row) in data.iterrows():
        if row.day == day and row.month == month: #if day is today and month is also today:
            name = row['name']
            #print(name)
            #print("today is the day!")

            #get a hold on the texts randomly
            random_letter = random.choice(os.listdir("./letter_templates"))
            with open(f"./letter_templates/{random_letter}") as letter:
                content = letter.read()
                new_content = content.replace("[NAME]", f"{name}")
                #print(new_content)

            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
            # with the person's actual name from birthdays.csv

            email = row['email']
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs="lgzg90@hotmail.com", #irl use row['email']
                                    msg=f"Subject:Happz BD!\n\n{new_content}")
        else:
            print('email was not sent')








