#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00

    def opis(self):
        napis_opisu = (
            f"{self.nazwa} to {self.rodzaj} "
            f"koloru {self.kolor} "
            f"o wartości {self.wartosc} zł")
        return napis_opisu

# Ponizej umiesc swoj kod
Auto1 = Pojazd()
Pojazd.Auto1.nazwa = "Opel"
Auto1.kolor = "niebieskiego"
Auto1.wartosc = 500
# sprawdzenie kodu
print(Auto1.opis())
