from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #Window and Canvas sizes
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, width=600, height=1000, pady=15, padx=15)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        #Could also add text inside the Canvas, with a x and y location argument
        self.question_text = self.canvas.create_text(
            150,
            125,
            font=("arial", 20, "italic"),
            width=280,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Label with score
        self.label_score = Label()
        self.label_score.config(text=f"score: {0}", fg="white", bg=THEME_COLOR, font=("arial", 10, "italic"))
        self.label_score.grid(column=1, row=0, rowspan=1)

        #label with Question
        #self.label_q = Label()
        #self.label_q.config(text='', width=28, font=("arial", 15, "italic"))
        #self.label_q.grid(column=0, row=1, rowspan=2)

        #Question:{0}

        #True Button
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, pady=15, command=self.true_button)
        self.true_button.grid(row=2, column=1)

        #False Button
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, pady=15, command=self.false_button)
        self.false_button.grid(row=2, column=0)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_button(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)


    def false_button(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            print("yay")
        else:
            print("nay")
        self.window.after(1000)
        self.quiz.next_question()



