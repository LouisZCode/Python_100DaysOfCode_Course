#this is what we want to do (that may cause an error):
try:
    #opening a file, that may not exists
    file = open("file_a.txt")
    #printing a key in a dictionary that does not exist
    a_dictionary = {"key" : "Value"}
    print(a_dictionary["gguguagag"])

#This is what we want to happen in case the error happens:
except FileNotFoundError:    #We found the exact error class we needed for File try
    #if there is no file, we create one!
    file = open("file_a.txt", "w")
    file.write("something")

#Same as before, BUT we can get hold of the error message:
except KeyError as error_message:
    print(f"the Key {error_message} does not exist")
    #Better for UX/UI and not crashing the program!

#This executes when try succeds!!  Else meant (if Try True:)
else:
    content = file.read()
    print(content)
    #NOTE if one of the except got triggered, then this else will never happen

#This is gonna run no matter what happens!
finally:
    file.close()
    print("file was closed")
    #Not so used! but important for certain cases.