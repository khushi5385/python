import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill=color, outline=color)

def clear_canvas():
    canvas.delete("all")

# Main window
root = tk.Tk()
root.title("Drawing Canvas")

# Canvas to draw on
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack()

# Color and clear button
color = "black"
clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack(pady=10)

# Bind mouse drag to draw
canvas.bind("<B1-Motion>", draw)

root.mainloop()

