import tkinter as tk


def mathgame():
    power.destroy()
    button.destroy()
    butt.destroy()
    import numbers
    numbers

def spellinggame():
    power.destroy()
    button.destroy()
    butt.destroy()
    import spellingtest
    spellingtest



window = tk.Tk()
window.title("Apex Fighters")
window.geometry("300x300")

power = tk.Label(text="Welcome to the Game.\n Select the game you want.")
power.pack()

button = tk.Button(text="Math game",
                  command=mathgame)
button.pack()

butt = tk.Button(text="Spelling game",
                  command=spellinggame)
butt.pack()

tk.mainloop()