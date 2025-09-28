import string
import random
from tkinter import *

# Fenster erstellen
variable = Tk()
variable.title("Passwort Generator")

# Globale Variablen
password = []
checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()
a = 0  # Passwortlänge

# Funktion: Passwortlänge speichern
def store_length():
    global a
    length = key_input.get()
    try:
        a = int(length)
    except ValueError:
        display.delete(0, END)
        display.insert(0, "Bitte eine gültige Zahl eingeben!")

# Funktion: Passwort generieren und anzeigen
def store_selection():
    display.delete(0, END)
    password.clear()

    characterList = ""  # Zeichenliste neu definieren (wird jedes Mal geleert)

    if checkvar1.get() == 1:
        characterList += string.ascii_letters
    if checkvar2.get() == 1:
        characterList += string.digits
    if checkvar3.get() == 1:
        characterList += string.punctuation

    if characterList == "":
        display.insert(0, "Bitte mindestens eine Option wählen!")
        return

    if a <= 0:
        display.insert(0, "Bitte eine gültige Länge eingeben!")
        return

    for i in range(a):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    password_text = "".join(password)
    display.insert(0, password_text)

# GUI-Elemente
ask_length = Label(variable, text="Enter password length:")
ask_length.grid(row=0)
key_input = Entry(variable)
key_input.grid(row=0, column=1)
key_input_button = Button(variable, text="Ok", command=store_length)
key_input_button.grid(row=0, column=2)

# Checkboxen
cb1 = Checkbutton(variable, text="Letters", variable=checkvar1, onvalue=1, offvalue=0)
cb1.grid(row=2, column=0)
cb2 = Checkbutton(variable, text="Digits", variable=checkvar2, onvalue=1, offvalue=0)
cb2.grid(row=2, column=1)
cb3 = Checkbutton(variable, text="Special characters", variable=checkvar3, onvalue=1, offvalue=0)
cb3.grid(row=2, column=2)

# Passwort-Anzeige
Random_password = Label(variable, text="Password")
Random_password.grid(row=3, column=0)
display = Entry(variable, width=40)
display.grid(row=3, column=1)

# Button zum Generieren
generate_button = Button(variable, text="Generate", command=store_selection)
generate_button.grid(row=3, column=2)

# GUI starten
variable.mainloop()
