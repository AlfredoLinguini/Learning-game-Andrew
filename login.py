import tkinter as tk
import os

def save_username(username):
    with open("usernames.txt", "a") as file:
        file.write(username + "\n")

def login(username):
    root.destroy()
    save_username(username)
    os.system("python main.py")

def login_button_clicked():
    username = entry.get()
    if username:
        login(username)

def check_username(username):
    with open("usernames.txt", "r") as file:
        return username in file.read().splitlines()

root = tk.Tk()
root.title("Username Login")

label = tk.Label(root, text="Enter your username:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login_button_clicked)
login_button.pack()

root.mainloop()