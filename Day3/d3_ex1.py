#Python Pizza Delivery Program! Welcome the costumer
print("Welcome to the Pizaa Delivery!")
#Create a value that will add different values when a choice is made:
pizza_cost = 0

#Lets add the cost of Size depending on the size selected
size = input("What size do you want the pizza?\nPlease select S, M or L\n").upper()

if size == "S":
    pizza_cost += 15
elif size == "M":
    pizza_cost += 20
elif size == "L":
    pizza_cost += 25
else:
    print("We dont have that size, please try again!")

#So far so good // print(pizza_cost)

pepperoni = input("Would you like to add pepperoni?\nSelect Y or N\n").upper() #You DO need the () to call these

if size == "S" and pepperoni == "Y":
    pizza_cost += 2
elif pepperoni == "Y":
    pizza_cost += 3
elif pepperoni == "N":
     pizza_cost += 0
else:
    print("I am not understanding you, lets try this all over again!")

#So far so good 2 // print(pizza_cost)

extra_cheese = input("Would you like cheese with your order?\nSelect Y or N\n").upper()

if extra_cheese == "Y":
    pizza_cost += 1

print(f"Thank you! your pizza will be \n${pizza_cost}")

#No questions on this one! looks like If statements, Elif and Else are on the bag... need to be careful with details and that is it.
