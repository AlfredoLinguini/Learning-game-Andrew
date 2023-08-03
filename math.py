import tkinter as tk

print("my balls")

def back():
    butto.destroy()
    pow.destroy()
    import main
    main

pow = tk.Label(text="This is math.")
pow.pack()

butto = tk.Button(text="Back Button",
                  command=back)
butto.pack()

tk.mainloop()