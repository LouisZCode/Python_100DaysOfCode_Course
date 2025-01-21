#Some UX, and guidance, welcome the player!
print("Welcome to the Band Name Generator")

#Here we request the data in form of String types, also adding a \n so it looks better
#we get the data into variables, so we can use them later
city_name = input("What is the name of the city you live in? \n")
pet_name = input("and what about your pets name? \n")

#we fuse the result into a last string, with a space after : and then the 2 variables. 
#As these are strings, they will just mash together
print("The name of your band is: " + city_name + pet_name)
