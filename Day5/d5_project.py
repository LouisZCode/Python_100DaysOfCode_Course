#Create a Password Generator...!

#we will need the random module, so...
import random

new_list = []
final_pass = ''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#We need to ask the user for the number of each one of the lists.. so N symbols, N letters, N Numbers:
N_letters = int(input("How many letters do your pass need?\n"))   #they will be all integer data types:
N_numbers = int(input('How many numbers do your pass need?\n'))
N_symbols = int(input('How many symbols do your pass need?\n'))

#Ok, so far we get the input, now, what do we do with it? Random choice?
#NO, we print 3 random choices from the list... but now better, we can put all these in a new list:
#for this, use APPEND thingy


#From lesson, no need to create a new list, we can directly add the element to the final_pass:
#for i in range(1, N_letters +1):
    #final_pass += random.choice(letter)        ___but how will you random this at the end??


#uodate, N the list was a great idea!! because that way we can shuffle it, YEY!

for i in range(N_letters):
    i = random.choice(letters)
    new_list.append(i)

for i in range(N_numbers):
    i = random.choice(numbers)
    new_list.append(i)

for i in range(N_symbols):
    i = random.choice(symbols)
    new_list.append(i)

#shffle this last list made of random elements taken from the lists
random.shuffle(new_list)

#We add all the shuffles elements into a string:
for i in new_list:
    final_pass += (str(i))

#Alternative, to use the weird symbol and end, so we dont print all elements below, but in a nice string?
#maybe, but this worked!

#We give the feedback to the user
print(f'Your new pass is:\n{final_pass}')