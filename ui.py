import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window = tkinter.Tk()
        self.window.title()

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_lable = tkinter.Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_lable.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text', fill=THEME_COLOR,
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_logo = tkinter.PhotoImage('./images/true.png')
        self.true_button = tkinter.Button(image=true_logo, highlightthickness=0,command=self.true_press)
        self.true_button.grid(row=2, column=0)

        false_logo = tkinter.PhotoImage('./images/false.png')
        self.false_button = tkinter.Button(image=false_logo,highlightthickness=0,command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text = q_text)

    def true_press(self):
        self.quiz.check_answer("True")
    def false_press(self):
        self.quiz.check_answer("False")


