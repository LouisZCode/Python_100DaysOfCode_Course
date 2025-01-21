import datetime

#we can for example, get the current time in miliseconds!
now = datetime.datetime.now()
#print(now)   #prints a datetime object

#or tap in elements of the time
year = now.year
#print(year)  #print an int

"""if year == 2025:
    print("this is the year!")
else:
    print("not this one")"""

#we have month, day, minutes...down to minisecond
#days start counton from Monday, which (as we ar ein a computer, is a 0

#So lets capture a birthday:
date_of_birth = datetime.datetime(day=11, month=9, year=1990)
#we could put hour but...
print(date_of_birth)   #this sadly prints 1990-09-11 00:00:00