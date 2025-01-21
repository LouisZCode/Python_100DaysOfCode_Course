import time
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#Create window
window = Tk()
window.config(bg=BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=50)
window.title("My own Anki!")

word = {}

# ---------------------------- SAVE and DELETE WORDS ACCORDINGLY ------------------------------- #
def save_word():
    global word
    """saves word to a new document so learn new words"""
    with open("./data/words_to_learn", 'w') as to_learn_doc:
        to_learn_doc.write(f"{word}")


def delete_word():
    """deletes words from the list, as you already know it"""
    pass

# ---------------------------- RANDOM WORD FROM French_Words ------------------------------- #
def next_word():
    global word, timer
    window.after_cancel(timer)
    canvas.itemconfig(canva_image, image=front_img)

    with open("./data/french_words.csv") as french_words:
        words_data = pandas.read_csv(french_words) #this is the data frame
        #Get the Serie:
        words_dict = words_data.to_dict(orient="records")
        random_word = random.randint(0,len(words_data) -1)
        word_in_column = (words_dict[random_word]["French"] )

        label_word.config(text=word_in_column, bg="white", fg="black")
        label_title.config(text="French", bg="white", fg="black")

        word = random_word

    timer = window.after(3000, give_answer)


def next_word_correct():
    delete_word()

    global word, timer
    window.after_cancel(timer)
    canvas.itemconfig(canva_image, image=front_img)

    with open("./data/french_words.csv") as french_words:
        words_data = pandas.read_csv(french_words) #this is the data frame
        #Get the Serie:
        words_dict = words_data.to_dict(orient="records")
        random_word = random.randint(0,len(words_data) -1)
        word_in_column = (words_dict[random_word]["French"] )

        label_word.config(text=word_in_column, bg="white", fg="black")
        label_title.config(text="French", bg="white", fg="black")

        word = random_word

    timer = window.after(3000, give_answer)


def next_word_incorrect():
    save_word()

    global word, timer
    window.after_cancel(timer)
    canvas.itemconfig(canva_image, image=front_img)

    with open("./data/french_words.csv") as french_words:
        words_data = pandas.read_csv(french_words) #this is the data frame
        #Get the Serie:
        words_dict = words_data.to_dict(orient="records")
        random_word = random.randint(0,len(words_data) -1)
        word_in_column = (words_dict[random_word]["French"] )

        label_word.config(text=word_in_column, bg="white", fg="black")
        label_title.config(text="French", bg="white", fg="black")

        word = random_word

    timer = window.after(3000, give_answer)

# ---------------------------- RANDOM WORD FROM French_Words ------------------------------- #

def give_answer():

    with open("./data/french_words.csv") as french_words:
        words_data = pandas.read_csv(french_words) #this is the data frame
        #Get the Serie:
        words_dict = words_data.to_dict(orient="records")
        random_word = random.randint(0,len(words_data) -1)
        word_in_column = (words_dict[word]["English"] )
        label_word.config(text=word_in_column)
        label_title.config(text="English")

    canvas.itemconfig(canva_image, image=back_img)
    label_word.config(bg="#91c2af", fg="white")
    label_title.config(bg="#91c2af", fg="white")
    label_title.config(text="English")

# ---------------------------- UI SETUP ------------------------------- #
timer = window.after(3000, give_answer)

#Create images for UI in place
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#front image to canvas
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canva_image = canvas.create_image(400, 270, image=front_img)
canvas.grid(column=1, row=2, columnspan=2, rowspan=2)

#BUTTONS
good_img = PhotoImage(file="./images/right.png")
button_right =Button(image=good_img)
button_right.config(highlightthickness=0, command=next_word_correct)
button_right.grid(column=2, row=4, columnspan=1)

bad_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=bad_img)
button_wrong.config(highlightthickness=0, command=next_word_incorrect)
button_wrong.grid(column=1, row=4, columnspan=1)

#LABELS:
label_title = Label(text="Title")
label_title.config(font=("Arial", 20, "italic"), bg="white")
label_title.grid(column=1, row=2, rowspan=1, columnspan=2)

label_word = Label(text="WORD")
label_word.config(font=("Arial", 50, "bold"), bg="white")
label_word.grid(column=1, row=2, columnspan=2, rowspan=2)


next_word()

#maintain window open until clicking close button
window.mainloop()