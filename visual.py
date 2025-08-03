import tkinter as tk
from tkinter import scrolledtext

# Send message from User 1
def send_user1(event=None):
    msg = entry1.get()
    if msg:
        display_message("User 1", msg, "#D1E7DD")
        entry1.delete(0, tk.END)

# Send message from User 2
def send_user2(event=None):
    msg = entry2.get()
    if msg:
        display_message("User 2", msg, "#F8D7DA")
        entry2.delete(0, tk.END)

# Function to show the message in the chat area
def display_message(sender, message, bg_color):
    bubble = tk.Frame(chat_area, bg=bg_color, padx=10, pady=5)
    tk.Label(bubble, text=f"{sender}: {message}", bg=bg_color, wraplength=300).pack()
    chat_area.window_create(tk.END, window=bubble)
    chat_area.insert(tk.END, "\n")
    chat_area.yview(tk.END)

# Main window
root = tk.Tk()
root.title("Two Person Chat")
root.geometry("450x500")
root.resizable(False, False)

# Chat display area with scroll
chat_area = tk.Text(root, wrap=tk.WORD, bg="white", state=tk.NORMAL)
chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)
chat_area.config(state=tk.NORMAL)

# Add scrollbar
scroll = tk.Scrollbar(chat_area)
chat_area.config(yscrollcommand=scroll.set)
scroll.config(command=chat_area.yview)

# User 1
frame1 = tk.Frame(root, bg="#EAF4F4")
frame1.pack(fill=tk.X, pady=5)
entry1 = tk.Entry(frame1, width=40)
entry1.pack(side=tk.LEFT, padx=5, pady=5)
entry1.bind("<Return>", send_user1)
btn1 = tk.Button(frame1, text="Send (User 1)", command=send_user1)
btn1.pack(side=tk.LEFT, padx=5)

# User 2
frame2 = tk.Frame(root, bg="#FDE2E4")
frame2.pack(fill=tk.X, pady=5)
entry2 = tk.Entry(frame2, width=40)
entry2.pack(side=tk.LEFT, padx=5, pady=5)
entry2.bind("<Return>", send_user2)
btn2 = tk.Button(frame2, text="Send (User 2)", command=send_user2)
btn2.pack(side=tk.LEFT, padx=5)

root.mainloop()
