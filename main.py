"""Main file."""
##################################
#  CALCULATOR v1.0 [14-11-2023]  #
##################################

#Use it as you want, but please don't pretend it's yours.
print("Made by pancracium @ github.com")

#Import necessary modules
import tkinter as tk
import math, re
from tooltip import Tooltip

class CalculatorApp:
    """Creates a class for the calculator app."""
    def __init__(self, master):
        self.master = master
        self.bind_keys()
        self.create_widgets()

    def bind_keys(self):
        self.master.bind("<s>", lambda event: self.button_click("sin"))
        self.master.bind("<t>", lambda event: self.button_click("tan"))
        self.master.bind("<c>", lambda event: self.button_click("cos"))
        self.master.bind("<x>", lambda event: self.button_click("·10^"))
        self.master.bind("<BackSpace>", lambda event: self.button_click("←"))
        self.master.bind("<p>", lambda event: self.button_click("π"))
        self.master.bind("<e>", lambda event: self.button_click("e"))
        self.master.bind("<f>", lambda event: self.button_click("∛"))
        self.master.bind("<l>", lambda event: self.button_click("log"))
        self.master.bind("1", lambda event: self.button_click("!"))
        self.master.bind("<g>", lambda event: self.button_click("^-1"))
        self.master.bind("<h>", lambda event: self.button_click("^2"))
        self.master.bind("<j>", lambda event: self.button_click("^3"))
        self.master.bind("<bracketleft>", lambda event: self.button_click("("))
        self.master.bind("<bracketright>", lambda event: self.button_click(")"))
        self.master.bind("7", lambda event: self.button_click("7"))
        self.master.bind("8", lambda event: self.button_click("8"))
        self.master.bind("9", lambda event: self.button_click("9"))
        self.master.bind("<r>", lambda event: self.button_click("√"))
        self.master.bind("<semicolon>", lambda event: self.button_click("^"))
        self.master.bind("4", lambda event: self.button_click("4"))
        self.master.bind("5", lambda event: self.button_click("5"))
        self.master.bind("6", lambda event: self.button_click("6"))
        self.master.bind("<equal>", lambda event: self.button_click("+"))
        self.master.bind("<minus>", lambda event: self.button_click("-"))
        self.master.bind("1", lambda event: self.button_click("1"))
        self.master.bind("2", lambda event: self.button_click("2"))
        self.master.bind("3", lambda event: self.button_click("3"))
        self.master.bind("<quoteright>", lambda event: self.button_click("x"))
        self.master.bind("<slash>", lambda event: self.button_click("÷"))
        self.master.bind("<a>", lambda event: self.button_click("C"))
        self.master.bind("0", lambda event: self.button_click("0"))
        self.master.bind(".", lambda event: self.button_click("."))
        self.master.bind("<Return>", lambda event: self.button_click("="))

    def create_widgets(self):
        """Creates the widgets. Kinda self-explainatory."""
        #Input (result and operations) box
        self.input_var = tk.StringVar()
        with open("log.txt", "r") as log:
            text = log.read()
            if text:
                self.input_var.set(text.split("=")[-1])
            else:
                self.input_var.set("")
            log.close()
        self.input_box = tk.Entry(self.master, textvariable=self.input_var, width=21, font=("Arial", 30),
                                  justify="right", bd=5, relief="flat", bg="gray70", fg="black",
                                  insertbackground="black", highlightcolor="black", highlightthickness=0,
                                  highlightbackground="gray", selectbackground="#c8c8c8",
                                  selectforeground="black", state="readonly")
        self.input_box.grid(row=0, column=0, columnspan=5, padx=8, pady=10)

        #Buttons
        self.create_button("sin", 1, 0)
        self.create_button("tan", 1, 1)
        self.create_button("cos", 1, 2)
        self.create_button("·10^", 1, 3)
        self.create_button("←", 1, 4)
        self.create_button("π", 2, 0)
        self.create_button("e", 2, 1)
        self.create_button("∛", 2, 2)
        self.create_button("log", 2, 3)
        self.create_button("!", 2, 4)
        self.create_button("^-1", 3, 0)
        self.create_button("^2", 3, 1)
        self.create_button("^3", 3, 2)
        self.create_button("(", 3, 3)
        self.create_button(")", 3, 4)
        self.create_button("7", 4, 0)
        self.create_button("8", 4, 1)
        self.create_button("9", 4, 2)
        self.create_button("√", 4, 3)
        self.create_button("^", 4, 4)
        self.create_button("4", 5, 0)
        self.create_button("5", 5, 1)
        self.create_button("6", 5, 2)
        self.create_button("+", 5, 3)
        self.create_button("-", 5, 4)
        self.create_button("1", 6, 0)
        self.create_button("2", 6, 1)
        self.create_button("3", 6, 2)
        self.create_button("x", 6, 3)
        self.create_button("÷", 6, 4)
        self.create_button("C", 7, 0)
        self.create_button("0", 7, 1)
        self.create_button(".", 7, 2)
        self.create_button("=", 7, 3, 2)


    def create_button(self, text:str, row:int, col:int, columnspan:int=1):
        """Creates the buttons."""
        if text != "=":
            #Create the equal button (=)
            button = tk.Button(self.master, text=text, width=7, height=3,
                            font=("Arial", 15), relief="flat", bg="gray75",
                            activebackground="gray60", borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
        else:
            #Create the other buttons
            button = tk.Button(self.master, text=text, width=16, height=3,
                            font=("Arial", 15), relief="flat", bg="gray75",
                            activebackground="gray60", borderwidth=0, highlightthickness=0,
                            command=lambda: self.button_click(text))
            button.grid(row=row, column=col, columnspan=columnspan, padx=5, pady=5)
        
        """        
        #Create a tooltip for each button (except the numbers)
        if text == "π":
            Tooltip(button, "Pi (3.141592654...).")
        elif text == "e":
            Tooltip(button, "Euler's identity (2.718281828...).")
        elif text == "∛":
            Tooltip(button, "Cube root.")
        elif text == "log":
            Tooltip(button, "Natural logarithm.")
        elif text == "←":
            Tooltip(button, "Delete last character.")
        elif text == "^-1":
            Tooltip(button, "Raise to the power of -1 (works like if you divided 1 by that number).")
        elif text == "^2":
            Tooltip(button, "Square.")
        elif text == "^3":
            Tooltip(button, "Cube.")
        elif text == "(":
            Tooltip(button, "Left bracket.")
        elif text == ")":
            Tooltip(button, "Right bracket.")
        elif text == "√":
            Tooltip(button, "Square root.")
        elif text == "^":
            Tooltip(button, "Raise a value to a power.")
        elif text == "+":
            Tooltip(button, "Add two values.")
        elif text == "-":
            Tooltip(button, "Subtract two values.")
        elif text == "x":
            Tooltip(button, "Multiply two values.")
        elif text == "÷":
            Tooltip(button, "Divide two values.")
        elif text == "C":
            Tooltip(button, "Clear the input box.")
        elif text == ".":
            Tooltip(button, "Insert a decimal point.")
        elif text == "=":
            Tooltip(button, "Calculate the result of the operations.")""" #Not yet, it adds a lot of bugs when pressing buttons...

    def button_click(self, text:str):
        """Handles the button clicks."""
        #Replace instances of brackets followed by a number with a multiplication symbol
        input_text = re.sub(r"(\))(\d)", r"\1*\2", self.input_var.get())
        input_text = re.sub(r'(\d)(\()', r'\1*\2', input_text)
        #Clear all the operations if the C (clear) button is clicked
        if text == "C":
            self.input_var.set("")
        #Calculate the result of the operations if the = (equal) button is clicked
        elif text == "=":
            try:
                if self.input_var.get():
                    result = eval(input_text)
                    result = round(result, 9)
                    self.input_var.set(str(result))
                    with open("log.txt", "w") as log:
                        log.write(f"\n{input_text}={result}")
                        log.close()
            except Exception as e:
                    self.input_var.set(f"Error: {e}")
                    return e
        #Add a multiplication symbol if the x (multiplication) button is clicked
        elif text == "x":
            self.input_var.set(input_text + "*")
        #Add a division symbol if the ÷ (division) button is clicked
        elif text == "÷":
            self.input_var.set(input_text + "/")
        #Calculate the square root of the operations if the √ (square root) button is clicked
        elif text == "√":
            try:
                result = math.sqrt(float(input_text))
                self.input_var.set(str(result))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
                return e
        #Calculate powers if the ^ (power) button or its variants are clicked
        elif text == "^":
            self.input_var.set(input_text + "**")
        elif text == "^-1":
            self.input_var.set(input_text + "**-1")
        elif text == "^2":
            self.input_var.set(input_text + "**2")
        elif text == "^3":
            self.input_var.set(input_text + "**3")
        #Add the pi number's value if the π (pi) button is pressed
        elif text == "π":
            self.input_var.set(input_text + str(math.pi))
        #Add the Euler's identity's value if the e (Euler's identity) button is pressed 
        elif text == "e":
            self.input_var.set(input_text + str(math.e))
        #Calculate the natural logarithm of the operations on the screen if the log (natural logarithm) button is pressed
        elif text == "log":
            try:
                result = math.log(float(input_text))
                self.input_var.set(str(result))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
                return e
        #Calculate the cube root of the operations on the input box if the ∛ (cube root) button is pressed
        elif text == "∛":
            try:
                result = round(float(input_text)**(1/3), 9)
                self.input_var.set(str(result))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
                return e
        #Calculate sin, tan and cos
        elif text == "sin":
            try:
                result = math.sin(float(self.input_var.get()))
                self.input_var.set(str(round(result, 9)))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
                return e
        elif text == "tan":
            try:
                result = math.tan(float(self.input_var.get()))
                self.input_var.set(str(round(result, 9)))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
                return e
        elif text == "cos":
            try:
                result = math.cos(float(self.input_var.get()))
                self.input_var.set(str(round(result, 9)))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
                return e
        #Calculate the factorial of the operations or number on the input box
        elif text == "!":
            try:
                result = math.factorial(int(self.input_var.get()))
                self.input_var.set(str(round(result)))
            except Exception as e:
                self.input_var.set(f"Error: {e}")
        elif text == "·10^":
            self.input_var.set(input_text + "*10**")
        #Detele the last character if the ← (backspace) button is pressed
        elif text == "←":
            self.input_var.set(input_text[:-1])
        #If the buttons from before are not the clicked ones, add the clicked button's text to the operation
        else:
            self.input_var.set(input_text + text)

#Create a window and set it up
WIDTH, HEIGHT = 495, 710
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}+{root.winfo_screenwidth() // 2 - WIDTH // 2}+{root.winfo_screenheight() // 2 - HEIGHT // 2}")
root.title("Calculator")
root.iconbitmap("icon.ico")
app = CalculatorApp(root)
root.mainloop()
