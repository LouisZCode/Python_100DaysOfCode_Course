
import random
import hangman_words

#first, we need to be able to generate  a random word:
random_word = random.choice(hangman_words.word_list)
print(random_word)

#create an emppty string and for each letter of the random word add 
placeholder = ''

for letter in range(len(random_word)):
   placeholder += '_'
print(placeholder)

#just a space for readibility
print('')


#create and empty display string, and loop troutgh the random word. the letters that match 
game_over = False
correct_letter = []
display = ''



while game_over == False:


    guess = input('please guess a letter:\n').lower()

    for letter in random_word:
        if letter == guess:
            correct_letter.append(guess)


        elif letter != guess:
            correct_letter.append('_')
    
    for i in correct_letter:
        display += (str(i))


    print(display)


