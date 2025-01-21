import smtplib

my_email = "luis.python.test1@gmail.com"
my_password = "pspw dyul oigd ciua"

connection = smtplib.SMTP("smtp.gmail.com", port=25) #Change the port to the used one,
# Google the port used for your provider

#lets encrypt the content quickly:
connection.starttls() #tls = Transport Layer Security

#not that the connection is secure, lets login
connection.login(user=my_email, password=my_password)
#and send an email
connection.sendmail(from_addr=my_email,
                    to_addrs="luis.python.test1@outlook.com",
                    msg="Subject:Greetings\n\nThis is the body of my Email")

#and now close the connection:
connection.close()


#NOTE
#We can do aaaaall this above, using the "with", "as" statement:
with smtplib.SMTP(host="smtp.gmail.com") as connection:
    """insert all the code above"""
    #you do NOT need to close the connection using this form!
    pass