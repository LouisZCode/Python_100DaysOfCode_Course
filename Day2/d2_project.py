#UX kind of welcoming
print("Welcome to the Tip Calculator!")

#Asking for all these data points, notice the FLOAT type and INT type.
#This could be better with a IF user inputs String...etc kinda thing, but not needed for the exercise
bill = float(input("How much was the bill? \n$"))
tip = int(input("how much tip would you like to give?\n%"))
number_people = int(input("and how many people will pay?\n"))

#Note: If you dont change the Type above, you cannot do Math! All inuts so far are str before Float or Int is added

#This is the calculation for the total bill, careful with the hierarchy!
total_bill = (bill + (bill*(tip/100))) /number_people

#Converted the totalbil to a string so to add it, also rounded it to 2 decimals before that!
print("Each one of you has to pay $" + str(round(total_bill, 2)))

#I forgot to use f"X" inside Print! that why I couldnt add it, so the "correcter" answer is:
#print(f"Each one of you has to pay ${round(total_bill, 2)}")

#question: how do I limit the number of decimals I get in the result?
#I used the round(X ,2) function.