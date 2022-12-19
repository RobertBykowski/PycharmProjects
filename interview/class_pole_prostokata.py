class Pole_prostokata:
    def __init__(self):
        print("Obiekt został utworzony")

    def __del__(self):
        print("Obiekt został usuniety")

    def czytaj_dane(self):
        self.a = float(input("Podaj bok a: "))
        self.b = float(input("Podaj bok b: "))

    def oblicz_pole(self):
        self.pole = self.a * self.b
        return self.pole

    def wyswietl_wynik(self):
        print(f"Pole prostokata o boku a={self.a} i boku b={self.b}"
              f" wynosi {self.pole}.")

pole1 = Pole_prostokata()
pole1.czytaj_dane()
pole1.oblicz_pole()
pole1.wyswietl_wynik()

