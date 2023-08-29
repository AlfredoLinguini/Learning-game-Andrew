import tkinter as tk

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

        power = tk.Label(self.current_frame, text="Welcome to the Game.\nSelect the game you want.")
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

        difficulty1 = tk.Button(self.current_frame, text="Level 1", command=self.level1math)
        difficulty1.pack()

        difficulty2 = tk.Button(self.current_frame, text="Level 2", command=self.level2math)
        difficulty2.pack()

        difficulty3 = tk.Button(self.current_frame, text="Level 3", command=self.level3math)
        difficulty3.pack()

        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_menu)
        back_button.pack()

    def show_spelling_game(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        pow = tk.Label(self.current_frame, text="Choose a difficulty.")
        pow.pack()

        difficulty1 = tk.Button(self.current_frame, text="Level 1", command=self.level1spelling)
        difficulty1.pack()

        difficulty2 = tk.Button(self.current_frame, text="Level 2", command=self.level2spelling)
        difficulty2.pack()

        difficulty3 = tk.Button(self.current_frame, text="Level 3", command=self.level3spelling)
        difficulty3.pack()

        back_button = tk.Button(self.current_frame, text="Back", command=self.show_main_menu)
        back_button.pack()

    def level1math(self):
        import numbers1
        numbers1
        pass

    def level2math(self):
        import numbers2
        numbers2
        pass

    def level3math(self):
        import numbers3
        numbers3
        pass

    def level1spelling(self):
        import spelling1
        spelling1
        pass

    def level2spelling(self):
        import spelling2
        spelling2
        pass

    def level3spelling(self):
        import spelling3
        spelling3
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()