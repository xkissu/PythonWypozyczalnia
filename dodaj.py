from tkinter import *
import flota
import datetime

class DodajAuto(Tk):
    def __init__(self):
        super().__init__()
        super().title("Dodaj auto")
        super().configure(background="black")
        global error
        error = ""
    def layout(self):

        global marka, model, rok, cena
        dodaj_auto = Label(self, text="Dodaj auto", bg="black", fg="white", font="none 12 bold")

        dodaj_marka = Label(self, text="Marka", bg="black", fg="white", font="none 10 bold")
        marka = Entry(self, width=20, bg="white")

        dodaj_model = Label(self, text="Model", bg="black", fg="white", font="none 10 bold")
        model = Entry(self, width=20, bg="white")

        dodaj_rok = Label(self, text="Rok", bg="black", fg="white", font="none 10 bold")
        rok = Entry(self, width=20, bg="white")

        dodaj_cena = Label(self, text="Cena", bg="black", fg="white", font="none 10 bold")
        cena = Entry(self, width=20, bg="white")
        global error_line
        error_line = Label(self, text="", bg="black", fg="red", font="none 10 bold")
        dodaj_button = Button(self, text="Dodaj", width=15, command=self.click)
        zamknij_button = Button(self, text="Zamknij", width=15, command=self.close_window)

        dodaj_auto.pack()
        dodaj_marka.pack()
        marka.pack()
        dodaj_model.pack()
        model.pack()
        dodaj_rok.pack()
        rok.pack()
        dodaj_cena.pack()
        cena.pack()
        error_line.pack()
        dodaj_button.pack()
        zamknij_button.pack()
    def click(self):
        if marka.get() == "" or model.get() == "" or rok.get() == "" or cena.get()=="":
            error_line.config(text="Wiersze nie moga byc puste")
            error_line.update()
        if marka.get().upper() in ["AUDI","BMW","MERCEDES","FORD","SKODA","KIA","OPEL","VOLKSWAGEN","PEUGEOT","RENAULT","CITROEN","HONDA","HYUNDAI","TOYOTA"]:
            try:
                if int(rok.get()) < 1900 or int(rok.get()) > int(str(datetime.date.today())[:4]):
                    error_line.config(text="Zly rok!")
                    error_line.update()
                else:
                    try:
                        if int(cena.get()) > 0:
                            error_line.config(text="Dodane!")
                            error_line.update()
                            auto = flota.flota()
                            auto.marka = marka.get().upper()
                            auto.model = model.get().upper()
                            auto.rok = rok.get()
                            auto.cena = cena.get()
                            baza = open("D:\Programowanie\Python\Wypozyczalnia/baza.txt", mode="r+")
                            try:
                                id = int(baza.readlines()[len(baza.readlines()) - 1].split(maxsplit=1)[0]) + 1
                            except IndexError:
                                id = 1
                            baza.write("\n{} {} {} {} {}".format(id, auto.marka, auto.model, auto.rok, auto.cena))
                            baza.close()
                            marka.delete(0, END)
                            model.delete(0, END)
                            rok.delete(0, END)
                            cena.delete(0, END)

                        else:
                            error_line.config(text="Cena mniejsza od 0!")
                            error_line.update()
                    except ValueError:
                        error_line.config(text="Cena musi byc liczba!")
                        error_line.update()
            except ValueError:
                error_line.config(text="Rok musi być liczbą!")
                error_line.update()
        else:
            error_line.config(text="Nieznana marka!")
            error_line.update()
    def close_window(self):
        self.destroy()