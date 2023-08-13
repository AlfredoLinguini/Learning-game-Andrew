import tkinter as tk
import random


def run():
    root = tk.Tk()
    game = SpellingGame(root)
    root.mainloop()


class SpellingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Game")


        self.words = ["apple", "banana", "cherry", "grape", "orange", "strawberry"]
        self.current_word = ""
        self.missing_letters = ""
        self.correct_answer = ""


        self.label = tk.Label(root, text="", font=("Helvetica", 24))
        self.label.pack(pady=20)


        self.entry = tk.Entry(root, font=("Helvetica", 18))
        self.entry.pack(pady=10)


        self.check_button = tk.Button(root, text="Check", command=self.check_answer)
        self.check_button.pack()


        self.next_button = tk.Button(root, text="Next Word", command=self.next_word)
        self.next_button.pack()

        self.next_word()


    def next_word(self):
        self.current_word = random.choice(self.words)
        self.missing_letters = "".join(random.sample(self.current_word, len(self.current_word) - 1))
        self.correct_answer = self.current_word


        self.label.config(text=self.missing_letters)
        self.entry.delete(0, tk.END)


    def check_answer(self):
        user_answer = self.entry.get()
        if user_answer == self.correct_answer:
            self.label.config(text="Correct!")
        else:
            self.label.config(text="Incorrect. Try again.")


if __name__ == "__main__":
    run()