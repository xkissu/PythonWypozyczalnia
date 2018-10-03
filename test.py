from tkinter import *
import flota

class DodajAuto(Tk):
    def __init__(self):
        super().__init__()
        super().title("Dodaj auto")
        super().configure(background="black")
        global error
        error = ""
    def layout(self):
        Label(self, text="Dodaj auto", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky=W)
        Label(self, text="Marka", bg="black", fg="white", font="none 10 bold").grid(row=1, column=0, sticky=W)
        global marka
        marka = Entry(self, width=20, bg="white")
        marka.grid(row=1, column=1, sticky=W)
        Label(self, text="Model", bg="black", fg="white", font="none 10 bold").grid(row=2, column=0, sticky=W)
        global model
        model = Entry(self, width=20, bg="white")
        model.grid(row=2, column=1, sticky=W)
        Label(self, text="Rok", bg="black", fg="white", font="none 10 bold").grid(row=3, column=0, sticky=W)
        global rok
        rok = Entry(self, width=20, bg="white")
        rok.grid(row=3, column=1, sticky=W)
        Label(self, text="Cena", bg="black", fg="white", font="none 10 bold").grid(row=4, column=0, sticky=W)
        global cena
        cena = Entry(self, width=20, bg="white")
        cena.grid(row=4, column=1, sticky=W)
        error_line = Label(self, text="", bg="black", fg="red", font="none 10 bold").grid(row=5, columnspan="3")
        Button(self, text="Dodaj", width=15, command=self.click).grid(row=6, column=0, sticky=W)
        Button(self, text="Zamknij", width=15, command=self.close_window).grid(row=6, column=1, sticky=W)
    def click(self):

        error = Label(self, text="", bg="black", fg="red", font="none 10 bold")
        error.pack()
        if marka.get() == "" or model.get() == "" or rok.get() == "" or cena.get()=="":
            error.config(text="siema")
            error.pack()

        else:
            error.destroy(self)
            auto = flota.flota()
            auto.marka = marka.get()
            auto.model = model.get()
            auto.rok = rok.get()
            auto.cena = cena.get()

            baza = open("D:\Programowanie\Python\Wypozyczalnia/baza.txt",mode="r+")

            id = int(baza.readlines()[len(baza.readlines()) - 1].split(maxsplit=1)[0]) + 1

            baza.write("\n{} {} {} {} {}".format(id, auto.marka,auto.model,auto.rok,auto.cena))
            baza.close()
            print("Dodane")
    def close_window(self):
        self.destroy()




