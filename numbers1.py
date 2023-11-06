import tkinter as tk
import random
from tkinter import PhotoImage
from PIL import Image
from PIL import ImageTk

class MathGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Game")
        self.root.geometry("400x200")

        self.score = 0
        self.num_questions = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
 
        self.generate_question()

        button = tk.Button(self.root, text="Close game", command=self.gameclose)
        button.pack()

    def gameclose(self):
        self.root.destroy()

    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        if random.choice([True, False]):
            self.answer = num1 + num2
            question_text = f"What is {num1} + {num2}?"
        else:
            if num1 < num2:
                num1, num2 = num2, num1
            self.answer = num1 - num2
            question_text = f"What is {num1} - {num2}?"

        self.question_label.config(text=question_text)
        self.answer_entry.delete(0, "end")
        self.result_label.config(text="")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == self.answer:
                self.score += 1
                self.result_label.config(text="Correct!", fg="green")
            else:
                self.result_label.config(text="Incorrect. Try again.", fg="red")
        else:
            self.result_label.config(text="Invalid input. Try again.", fg="red")

        self.num_questions += 1
        self.update_score()

        if self.num_questions < 10:
            self.generate_question()
        else:
            self.question_label.config(text="Game Over")
            self.answer_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

            if self.score == 10:
                self.result_label.config(text="Congratulations!!! You got all 10 questions correct.")
                image = Image.open("brain-big-brain.gif")
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(image=photo)
                label.pack()
                frameCnt = 54
                frames = [PhotoImage(file='brain-big-brain.gif', format='gif -index %i' % (i))
                          for i in range(frameCnt)]

                def update(ind):
                    frame = frames[ind]
                    ind += 1
                    if ind == frameCnt:
                        ind = 0
                    label.configure(image=frame)
                    self.root.after(100, update, ind)
                self.root.mainloop()
            

    def update_score(self):
        self.root.title(f"Math Game - Score: {self.score}/{self.num_questions}")

def run_math_game():
    math_game_root = tk.Tk()
    math_app = MathGameApp(math_game_root)
    math_game_root.mainloop()
    
