#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


"""We first create a list of the name with the lines in the invited_names.txt"""
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    list_names = (names.readlines())
    #list_names.strip()
    #print(list_names)

"""then we get a hold of the letter content"""
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    #print(letter_content.replace("[name]", list_names[]))



"""finally we replace the [name] with each name in the name list"""
for name in list_names:
    n_name = name.strip("\n")
    #print(name)
    final = letter_content.replace("[name]", n_name)
    print(final)
    #and we create each file in the directory with the "x" call, and then write the final letter on each!
    open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{n_name}.txt", "w").write(final)






