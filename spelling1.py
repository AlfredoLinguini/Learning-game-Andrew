import tkinter as tk
import random
import string

def run():
    root = tk.Tk()
    game = SpellingGame(root)
    root.mainloop()

class SpellingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Game")
        power = tk.Label(text="Find the missing letter.")
        power.pack()

        self.words = {
            "pple": "apple",
            "bnana": "banana",
            "cerry": "cherry",
            "grap": "grape",
            "orage": "orange"
        }

        self.current_word = ""
        self.correct_answer = ""
        self.score = 0

        self.label = tk.Label(root, text="", font=("Cambria Math", 25))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Cambria Math", 20))
        self.entry.pack(pady=10)

        self.check_button = tk.Button(root, text="Check", command=self.check_answer)
        self.check_button.pack()

        self.next_button = tk.Button(root, text="Next Word", command=self.next_word)
        self.next_button.pack()

        self.score_label = tk.Label(root, text="", font=("Cambria Math", 15))
        self.score_label.pack(pady=10)

        self.next_word()

    def next_word(self):
        if not self.words:
            self.label.config(text="No more words!")
            self.score_label.config(text="Final Score: " + str(self.score))
            return

        self.current_word = random.choice(list(self.words.keys()))
        self.correct_answer = self.words[self.current_word]
        del self.words[self.current_word]

        self.label.config(text=self.current_word)
        self.entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.entry.get()
        if user_answer == self.correct_answer:
            self.label.config(text="Correct!")
            self.score += 1
        else:
            self.label.config(text="Incorrect. Try again.")

run()