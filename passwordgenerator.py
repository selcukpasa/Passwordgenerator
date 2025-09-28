import string 
import random 
from tkinter import * 
import tkinter as tk 
  
variable = Tk() 
variable.title("Passwort Generator") 

characterList = "" 
password = [] 
checkvar1 = IntVar() 
checkvar2 = IntVar() 
checkvar3 = IntVar() 
a = 0 

def store_length(): 
    global a 
    length = key_input.get() 
    a = int(length)

def store_selection():
    display.delete(0, END)
    password.clear() 
    global characterList 
    if checkvar1.get() == 1: 
        characterList += string.ascii_letters 
    if checkvar2.get() == 1: 
        characterList += string.digits 
    if checkvar3.get() == 1: 
        characterList += string.punctuation 
    for i in range(a): 
        randomchar = random.choice(characterList) 
        password.append(randomchar)
    password_text = "".join(password)
    display.insert(10, password_text)

ask_length = Label(variable, text="Enter password length: ") 
ask_length.grid(row=0)
key_input = Entry(variable) 
key_input.grid(row=0, column=1) 
key_input_button = Button(variable, text="Ok", command=store_length)
key_input_button.grid(row=0, column=2,)

cb1 = Checkbutton(variable, text="Letters", variable = checkvar1, onvalue = 1, offvalue = 0)
cb1.grid(row=2, column=0)
cb2 = Checkbutton(variable, text="Digits", variable = checkvar2, onvalue = 1, offvalue = 0)
cb2.grid(row=2, column=1)
cb3 = Checkbutton(variable, text="Special characters", variable = checkvar3, onvalue = 1, offvalue = 0)
cb3.grid(row=2, column=2)

Random_password = Label(variable, text = "Password") 
display = Entry(variable, width = 40) 
display.grid(row=3, column=1) 

generate_button = Button(variable, text="Generate", command=store_selection)
generate_button.grid(row=3, column=2)

variable.mainloop() 
