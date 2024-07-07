import tkinter as tk
import random

def hiku():
    randomNum = random.randint(1,3)
    if randomNum == 1:
        label.config(text="大吉")
    elif randomNum == 2:
        label.config(text="中吉")
    else:
        label.config(text="小吉")
    
root = tk.Tk()
root.title("おみくじ")
root.geometry("500x500")

label = tk.Label(root, text = "")
label.pack()

button = tk.Button(root, text="引く", command=hiku)
button.pack(pady=10)

root.mainloop()