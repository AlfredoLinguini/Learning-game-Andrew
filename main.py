import tkinter as tk
import os
from tkinter import *
class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learning Game")
        self.root.geometry("300x300")

        self.current_frame = None

        self.show_main_menu()

    def show_main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        power = tk.Label(self.current_frame, text="Welcome to the Game.\nSelect the game you want to play.")
        power.pack()

        button = tk.Button(self.current_frame, text="Math game", command=self.show_math_game)
        button.pack()

        butt = tk.Button(self.current_frame, text="Spelling game", command=self.show_spelling_game)
        butt.pack()

    def show_math_game(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        pow = tk.Label(self.current_frame, text="Choose a difficulty.")
        pow.pack()

        difficulty1math = tk.Button(self.current_frame, text="Level 1", command=self.level1math)
        difficulty1math.pack()

        difficulty2math = tk.Button(self.current_frame, text="Level 2", command=self.level2math)
        difficulty2math.pack()

        difficulty3math = tk.Button(self.current_frame, text="Level 3", command=self.level3math)
        difficulty3math.pack()

        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_menu)
        back_button.pack()

    def show_spelling_game(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        pow = tk.Label(self.current_frame, text="Choose a difficulty.")
        pow.pack()

        difficulty1spelling = tk.Button(self.current_frame, text="Level 1", command=self.level1spelling)
        difficulty1spelling.pack()

        difficulty2spelling = tk.Button(self.current_frame, text="Level 2", command=self.level2spelling)
        difficulty2spelling.pack()

        difficulty3spelling = tk.Button(self.current_frame, text="Level 3", command=self.level3spelling)
        difficulty3spelling.pack()

        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_menu)
        back_button.pack()

    def run_level1math_game(self):
        math_game_root = tk.Tk()
        math_app = MathGameApp(math_game_root)
        math_game_root.mainloop()

    def level1math(self):
        import numbers1
        numbers1.run_math_game()

    def level2math(self):
        import numbers2
        numbers2.runmath2()

    def level3math(self):
        import numbers3
        numbers3.runmath3()

    def level1spelling(self):
        import spelling1
        spelling1.spellgame1()

    def level2spelling(self):
        import spelling2
        spelling2.spellgame2()

    def level3spelling(self):
        import spelling3
        spelling3.spellgame3()

def login(username):
    global current_username
    current_username = username
    root.destroy()
    os.system("python main.py")

root = tk.Tk()
app = GameApp(root)
root.mainloop()