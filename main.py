"""Main file."""

##################################
#  CALCULATOR v0.5 [22-03-2023]  #
##################################

#Import necessary modules
import tkinter as tk
from app import CalculatorApp

#Create a window and set it up
root = tk.Tk()
app = CalculatorApp(master=root, width=495, height=710)
app.master.mainloop()