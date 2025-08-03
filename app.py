from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/weather')
def weather():
    city = request.args.get('city', 'your city')
    return render_template("weather.html", city=city)


if __name__ == '__main__':
    app.run(debug=True)




















    import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", bd=8, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()

print("enter 1 to 8")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")
print("7. Floor Division")
print("8. Bitwise AND")
n = int(input("Enter a number: "))
3
a = int(input("enter no"))
b = int(input("enter no"))
print("You entered:", n, a, b)
def demo(a,b):
       
    c = a + b 
    return c

def demo1(a,b):
    
    c = a - b
    return c


def demo2(a,b):
   
    c = a * b
    return c    


def demo3(a,b):
                                
    c = a/ b
    return c

def demo4(a,b):
    c = a % b
    return c

def demo5(a,b):
    c = a ** b
    return c

def demo6(a,b):
    c = a // b
    return c

def demo7(a,b):
    c = a & b
    return c
 
def demo8(a,b):
    c = a | b
    return c


if ( n == 1):
    print("Addition is: ", demo(a,b))
elif ( n == 2):
    print("Subtraction is: ", demo1(a,b))
elif ( n == 3):
    print("Multiplication is: ", demo2(a,b))
elif ( n == 4):
    print("Division is: ", demo3(a,b))
elif ( n == 5):
    print("Modulus is: ", demo4(a,b))
elif ( n == 6):
    print("Exponentiation is: ", demo5(a,b))
elif ( n == 7):
    print("Floor Division is: ", demo6(a,b))
elif ( n == 8):
    print("Bitwise AND is: ", demo7(a,b))
else:   
   print( "Invalid input, please enter a number between 1 and 4.")










   # calculator 
   import tkinter as tk

def calculate_expression(expr):
    try:
        # Extract numbers and operator manually
        for op in ["**", "//", "&", "|", "+", "-", "*", "/", "%"]:
            if op in expr:
                a, b = expr.split(op)
                a = int(a.strip())
                b = int(b.strip())

                if op == "+":
                    return str(a + b)
                elif op == "-":
                    return str(a - b)
                elif op == "*":
                    return str(a * b)
                elif op == "/":
                    return str(a / b) if b != 0 else "Error"
                elif op == "%":
                    return str(a % b)
                elif op == "**":
                    return str(a ** b)
                elif op == "//":
                    return str(a // b)
                elif op == "&":
                    return str(a & b)
                elif op == "|":
                    return str(a | b)
        return "Invalid"
    except:
        return "Error"

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        result = calculate_expression(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Set up the main window
root = tk.Tk()
root.title("Custom Calculator")

entry = tk.Entry(root, font="Arial 20", bd=8, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/", "//"],
    ["4", "5", "6", "*", "**"],
    ["1", "2", "3", "-", "%"],
    ["C", "0", "=", "+", "&"],
    ["|"]  # Bitwise OR (single button row)
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()

