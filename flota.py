
class flota():
    def __init__(self):
        print("Init auto")
        self.marka = ""
        self.model = ""
        self.rok = ""
        self.cena = ""
        self.wypozyczony = False
    def auto(self,marka,model,rok,cena,wypozyczony):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.cena = cena
        self.wypozyczony = wypozyczony
    def stan(self):
        if self.wypozyczony:
            print("{} {} jest wypozyczony".format(self.marka,self.model))
        else:
            print("{} {} nie jest wypozyczony".format(self.marka,self.model))