#Life in Weeks!

#Create a function called life_in_weeks() using maths and 
#f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.

def life_in_weeks(age):
    new_age = ((36 * 4) * age)
    print(f"You have {new_age} weeks left.")

life_in_weeks(20)