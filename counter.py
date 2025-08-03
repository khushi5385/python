import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=str(count))

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root, text="0", font="Arial 48")
label.pack()

btn = tk.Button(root, text="Click Me!", font="Arial 24", command=increase)
btn.pack(pady=10)

root.mainloop()
