#You are going to write a function called calculate_love_score() 
# that tests the compatibility between two names. 
# To work out the love score between two people: 

#1. Take both people's names and check for the number of times the
# letters in the word TRUE occurs.   

#2. Then check for the number of times the
# letters in the word LOVE occurs.   

#3. Then combine these numbers to make a
# 2 digit number and print it out. 

true = "true"
love = "love"

def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    totalnames = name1 + name2
    for i in true:
        if i in totalnames:
            true_score += 1
    for i in love:
        if i in totalnames:
            love_score += 1
    
    print(f"{true_score}{love_score}")



calculate_love_score("Kanye West", "Kim Kardashian")