from tkinter import *   #This is all the classes, not the modules included!
from tkinter import messagebox
import random
import json

from password_gene import password

TONE = "#EFE9F4"

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website_searched = entry_web.get()
    website = website_searched.capitalize()
    user_info = entry_user_data.get()
    #print(website)

    try:
        with open("data.json", "r") as data:
            dictionary = json.load(data)
            current_pass = dictionary[website]["password"]
            #entry_pass.insert(0, current_pass)

    except KeyError:
        #print("key does not exists")
        messagebox.showinfo(title="Your Information", message="This website is not in data")

    except TypeError:
        print("you need to write something!")

    else:
        messagebox.showinfo(title=f"your {website} password", message=f"username:{user_info}\n"
                                                                      f"password: {current_pass}")
        #entry_web.insert(0, f"{website}")
        #entry_pass.insert(0, dictionary[website]["password"])



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """Generates a password composed of random symbols, letters and numbers"""

    entry_pass.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for char in range(nr_letters)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]

    #print(f"this is pasword list:{letter_list}, and {number_list} and {symbol_list}")

    pass_list = letter_list + number_list + symbol_list
    random.shuffle(pass_list)

    password = "".join(pass_list)

    entry_pass.insert(0, password)
    print('pass generated!')
    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

#note = delet function
def add_pass():
    """Add all info to the data doc, deletes all info in 1 time use entry boxes"""
    #get a hold of all data at the moment
    user_info = entry_user_data.get()
    web_info = entry_web.get()
    password = entry_pass.get()

    new_data = {
        web_info.capitalize() : {
            "emal": user_info,
            "password": password
        }
    }

    if len(user_info) == 0 or len(web_info) == 0 or len(password) == 0:  #better to use len(data) as == "" accept spaces!
        messagebox.showinfo(title="WARNING", message="Fields can not be empty, please ty again")

    else:
        try:
            with open("data.json", "r") as new_doc:
                #to update a json file with new data, is a 3 step approach:

                #1- read form a json old data
                data = json.load(new_doc)

        except FileNotFoundError:
            #if there is no file, we catch the error, and we create the file
            with open("data.json", "w") as new_doc:
                json.dump(new_data, new_doc, indent=4)

        else:
            with open("data.json", "w") as new_doc:
                # 2- Updating old data with new data
                data.update(new_data)
                #3 Saving updated data
                json.dump(data, new_doc, indent=4)

        finally:
            #deletes all info in used entries
            delete_info()

            #to check if all was done:
            #To make a pop up?  #later: YES
            #print('all info sent to Doc!')

            messagebox.showinfo(title="DATA SENT", message="Your information has been saved into your Data document")


def delete_info():
    """deletes all info in entry boxes. Called in add-pass()"""
    entry_pass.delete(0, END)
    entry_web.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=TONE)
window.title("Password Manager")


#create canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=TONE)


#Buttons
button_pass_gen = Button(text="Generate Pass", width=14, command=generate_pass)
button_pass_gen.grid(column=2, row=3)

button_search = Button(text="Search", width=14, command=search_website)
button_search.grid(column=2, row=1)

button_add_pass = Button(text="Add", width=29, command=add_pass)
button_add_pass.grid(column=1, row=4, columnspan=2)


#image to a variable and then to canvas:
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)


#Labels
label_website = Label(text="Website Name:", bg=TONE)
label_website.grid(column=0, row=1)

label_user_data= Label(text="Username/Email:", bg=TONE)
label_user_data.grid(column=0, row=2)

label_pass = Label(text="Password:", bg=TONE)
label_pass.grid(column=0, row=3)


#data Entry(s)
entry_web = Entry(width=25)
entry_web.focus_set()
entry_web.grid(column=1, row=1, columnspan=1)


entry_user_data = Entry(width=25)
entry_user_data.insert(0, "lgzg90@hotmail.com")
entry_user_data.grid(column=1, row=2, columnspan=1)


entry_pass = Entry(width=25)
entry_pass.grid(column=1, row=3)


window.mainloop()