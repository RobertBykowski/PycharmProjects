class Dzialanie:
    def __init__(self, liczba_A, liczba_B):
        self.liczba_A = liczba_A
        self.liczba_B = liczba_B


    def dodaj(self):
        return (self.liczba_A + self.liczba_B)
    def odejmowanie(self):
        return (self.liczba_A - self.liczba_B)
    def mnozenie(self):
        return (self.liczba_A * self.liczba_B)
    def drukuj(self):
        return "Liczba 1 {} | liczba 2 {}".format(self.liczba_A, self.liczba_B)

liczby_1 = Dzialanie(10, 12)
liczby_2 = Dzialanie(10, 12)


print(f"Wynik dodawania dla {liczby_1.liczba_A} + {liczby_1.liczba_B} = {Dzialanie.dodaj(liczby_1)}")
print(f"Wynik mnożenia dla  {liczby_1.liczba_A} * {liczby_1.liczba_B} = {Dzialanie.mnozenie(liczby_2)}")


