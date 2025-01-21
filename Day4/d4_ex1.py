#Random business card challenge!
#Get the RANDOM() Module
import random

#Create a list with Names
people_list = ['david', 'luis', 'Pedro', 'maria']

#Can take any arrays! so random.choice works with this vlaue:
string = "Hello"

#print a random choice in this list:
print(random.choice(people_list))

#alternative:
print(random.randint(0,3))
#and just add this number to the indey for print!

#another option: print(random.choice(string))