import tkinter as tk

def osita():
    decimal_value = int(entry.get())
    binary_value = bin(decimal_value)[2:]
    label_result.config(text=binary_value)

root = tk.Tk()
root.title("１０進数変換")
root.geometry("500x500")

label = tk.Label(root, text="１０進数から２進数に変換")
label.pack(pady=10)
entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Convert", command=osita)
button.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()