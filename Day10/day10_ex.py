
"""
A normal year has 365 days, leap years have 366,

This is how you work out whether if a particular year is a leap year. 
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder 
- unless the year is also divisible by 400 with no remainder  
"""

def is_leap_year(year):

    if year % 4 == 0 and year % 100 != 1:
        print(True)

    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(True)
    
    else:
        print(False)


is_leap_year(2000)
is_leap_year(2400)
is_leap_year(1989)
is_leap_year(2100)

"""
Solution from the exercise:

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

I like the staking of IF statements..!!
Also, notice that there is the Return True, but no way to see that in the Terminal!
"""