import tkinter
#you can also import EVERYTHiNG with *, so you dont need to att tkinker.Class everytime
#    from tkinter import *

window = tkinter.Tk()
window.title("Converter")
window.minsize(500, 300)
window.config(padx=20, pady=20)  #Padding is space on the axys..!

#Labels
my_label = tkinter.Label(text="Come on, do it!", font=("Arial", 24, "bold"))
#there are different ways to change the text in here, check the documentation! https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
my_label["text"] = "New Text"
my_label.config(text="Come on, do it!")
"""my_label.pack()"""   #this makes it show it on screen
#my_label.place(x=150,y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#Buttons
def button_clicked():
    my_label.config(text=input.get())
button = tkinter.Button(text="click me!", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=5, pady=5)

new_button = tkinter.Button(text="I am a new button", command=button_clicked)
new_button.grid(column=3, row=0)
new_button.config(padx=5, pady=5)

#inputs
input = tkinter.Entry(width=30)
"""input.pack()"""   #You cannot use pack with GRID at the same time!
input.grid(column=4, row=3)


window.mainloop()