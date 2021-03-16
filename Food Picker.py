# This is a sample Python script.

import random

from tkinter import *

def print_hi(name):
    print(random.choice(Dictionary.get(name)))

Dictionary = {'snacks': ['cheetos', 'brownies', 'cookies'],
              'meals': ['spaggetti', 'burger', 'ham'],
              'lol': ['fart!']}

#code for random food selection
def snack():
    generatedFood = random.choice(Dictionary.get('snacks'))
    output.delete(0.0, END)
    output.insert(END, generatedFood)

def meal():
    generatedFood = random.choice(Dictionary.get('meals'))
    output.delete(0.0, END)
    output.insert(END, generatedFood)

def lol():
    generatedFood = random.choice(Dictionary.get('lol'))
    output.delete(0.0, END)
    output.insert(END, generatedFood)

#code for my window

window = Tk()
window.title("what we eating boys")
window.configure(background="black")

#label

Label(window, text="Click the meal you would like a random selection from", bg= "black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

#buttons
Button(window, text="Snacks", width=6, command=snack) .grid(row=3, column=0, sticky=W)
Button(window, text="Meals", width=5, command=meal) .grid(row=4, column=0, sticky=W)
Button(window, text="lol", width=3, command=lol) .grid(row=5, column=2, sticky=W)

#output text box
output = Text(window, width=75, height = 6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#run window
window.mainloop()