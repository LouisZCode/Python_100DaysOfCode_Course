"""    file = open("my_file.txt")
    You better use the next one tho

    with open("my_file.txt") as file:
        #indented actions
        #now you dont need the .close()

    contents = file.read()
    print(contents)
    file.close()

    #you can also write in the file:
    with open("my_file.txt") as newfile:
        newfile.write("Hello my friends..! ")
"""