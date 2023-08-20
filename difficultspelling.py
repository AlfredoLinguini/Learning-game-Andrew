import tkinter as tk

def back():
    butto.destroy()
    pow.destroy()
    difficulty1.destroy()
    difficulty2.destroy()
    difficulty3.destroy()
    import main
    main

def level1():
    pow.destroy()
    butto.destroy()
    difficulty1.destroy()
    difficulty2.destroy()
    difficulty3.destroy()
    import spelling1
    spelling1

def level2():
    pow.destroy()
    butto.destroy()
    difficulty1.destroy()
    difficulty2.destroy()
    difficulty3.destroy()
    import spelling2
    spelling2

def level3():
    pow.destroy()
    butto.destroy()
    difficulty1.destroy()
    difficulty2.destroy()
    difficulty3.destroy()
    import spelling3
    spelling3


pow = tk.Label(text="Choose a difficulty.")
pow.pack()

difficulty1 = tk.Button(text="Level 1",
                  command=level1)
difficulty1.pack()

difficulty2 = tk.Button(text="Level 2",
                  command=level2)
difficulty2.pack()

difficulty3 = tk.Button(text="Level 3",
                  command=level3)
difficulty3.pack()

butto = tk.Button(text="Back Button",
                  command=back)
butto.pack()