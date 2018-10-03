import dodaj
from tkinter import *

def click():
    window = dodaj.DodajAuto()
    window.layout()
def click2():
    print(dodaj.DodajAuto)

menu = Tk()
menu.title("Wypozyczalnia samochodow")
menu.configure(background="black")

Label(menu, text="Wypozyczalnia", bg="black", fg="white", font="none 12 bold").grid(columnspan=2, row=0, column=0, sticky=W)
Button(menu, text="Dodaj Auto", width=15, command=click).grid(row=1, column=1, sticky=W)
Button(menu, text="Wypozycz", width=15, command=click).grid(row=2, column=1, sticky=W)
Button(menu, text="TEST", width=15, command=click2).grid(row=3, column=1, sticky=W)

menu.mainloop()

#dodaj.DodajAuto()

