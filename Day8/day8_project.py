#Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# use the index() function


""" ENCRYPTION """
def encrypt(word):
    new_word = ""
    for char in word:
        x = alphabet.index(char)
        n = len(alphabet)
        x += number
        new_word += alphabet[x % n]
    print('\nThis is the new word:')
    print(new_word)
    print()


""" DECRYPTION """
def decrypt(word):
    new_word = ""
    for char in word:
        x = alphabet.index(char)
        n = len(alphabet)
        x -= number
        new_word += alphabet[x % n]
    print('\nThis is the original word:')
    print(new_word)
    print()


todo = input('Type "encode" to encrypt, type "decode" to decrpyt:\n').lower()

word = input("Type the word you want to encrypt\n")
number = int(input('type the number to unlock\n'))


if todo == 'encode':
    encrypt(word)
elif todo == 'decode':
    decrypt(word)






#What if the wod ens out or range= like w + 4
"""Use the Modulo ina  smart way!

>>> alphabet = ['a', 'b', 'c', 'd']
>>> n = len(alphabet)    #26
>>> alphabet[5 % n]
'b'

"""