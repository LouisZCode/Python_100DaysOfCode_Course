from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 1
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_count():
    global reps
    reps = 1
    global checks
    checks = ""

    window.after_cancel(timer)
    label_upper.config(text=f"Timer", bg=YELLOW, fg=RED)
    label_check.config(text=f"{checks}", bg=YELLOW, fg=RED)
    canvas.itemconfig(timer_text, text=f"00:00")
    canvas.config(bg=YELLOW)
    window.config(bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global checks
    #reps +=1
    print(checks)

    work_sec = WORK_MIN * 60
    short_brake = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps > 8:
        reset_count()

    elif reps == 8:
        # if it is the 8th
        count_down(long_break)
        reps += 1
        canvas.config(bg=GREEN), window.config(bg=GREEN)
        label_upper.config(text=f"L.Break", bg=GREEN, fg=RED)
        label_check.config(text= f"{checks}", bg=GREEN, fg=RED)
        checks = ""
        #reset_count()


    elif reps % 2 == 0:
        # if it is the 2nd/4th/6th
        count_down(short_brake)
        reps += 1
        label_upper.config(text="Break", bg="blue", fg=GREEN)
        canvas.config(bg="blue"), window.config(bg="blue")
        label_check.config(text=f"{checks}", bg="blue", fg=GREEN)

    else:
    #if it is the 2nd/4th/6th
        count_down(work_sec)
        reps += 1
        label_upper.config(text="Work!", bg=RED, fg=GREEN)
        canvas.config(bg=RED), window.config(bg=RED)
        label_check.config(text=f"{checks}", bg=RED, fg=GREEN)
        checks += "✔"

    #print(reps)

    #5 would be the final, now 1 for testing
    #count_down(1 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    #print(count)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    if count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    #print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


"""def say_something(a, b, c):
    print(a)
    print(b)
    print(c)

#this will call the function, and the value after is the parameter that goes into the function! aka. "Hello" is thing
window.after(1000, say_something,1, 3, 4) #is this like the timer in Godot? yes but more complex"""

#Create a canvas in the window...!
canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas_bg = canvas.config(bg= YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
#Create a text (clock numbers)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
#location of Canvas
canvas.grid(row=2, column=2)


#Text Label Above
label_upper = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label_upper.grid(row=0, column=2)

#checkmark label below
label_check = Label(text=f"{checks}", font=(FONT_NAME, 20, "bold"), bg=YELLOW)
label_check.grid(row=4, column=2)

#Start Button
button_start = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=PINK, fg="dark green", command=start_timer)
button_start.grid(row=3, column=0)

#Reset Button
button_reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=PINK, fg="dark green", command=reset_count)
button_reset.grid(row=3, column=3)


window.mainloop()  #this loops trought and check every second if something is happening..!