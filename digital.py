import tkinter as tk
import time

def update_time():
    current = time.strftime("%H:%M:%S")
    label.config(text=current)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 48), fg="white", bg="black")
label.pack(padx=20, pady=20)

update_time()
root.mainloop()
