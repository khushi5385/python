import tkinter as tk
from tkinter import filedialog

def save_file():
    content = text_area.get("1.0", tk.END)
    file = filedialog.asksaveasfile(defaultextension=".txt")
    if file:
        file.write(content)
        file.close()

root = tk.Tk()
root.title("Simple Notepad")

text_area = tk.Text(root, font="Arial 14")
text_area.pack(expand=True, fill='both')

save_btn = tk.Button(root, text="Save", command=save_file)
save_btn.pack()

root.mainloop()
 