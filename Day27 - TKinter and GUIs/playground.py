from tkinter import *

FONT = ("Arial", 10, "bold")
KMS = 0

window = Tk()
window.title("Miles to KM converter")
window.minsize(100, 50)
window.config(padx=20, pady=20)


#LABELS
label_iseq = Label(text="is equal to", font=FONT)
label_iseq.grid(column=0, row=1)

label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)

label_km = Label(text="Kms", font=FONT)
label_km.grid(column=2, row=1)

label_result = Label(text=f"{KMS}", font=FONT)
label_result.grid(column=1, row=1)
label_result.config(padx=10)

#INPUT
input = Entry(width=10)
input.grid(column=1, row=0)
input.focus()

#BUTTON
def miles2kms():
    """Convert miles to Kms"""
    data = input.get()
    float_miles = float(data) * 1.609344
    miles = round(float_miles,2)
    label_result.config(text=f"{miles}")

button = Button(text="convert", command=miles2kms)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)


window.mainloop()
