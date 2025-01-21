"""Project to improve the pandas project, search a key and use NATO dictionaries"""

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

def enter_word():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("sorry, only letters are allowed")
        enter_word()

    else:
        print(output_list)

enter_word()