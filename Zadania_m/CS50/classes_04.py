class Pracownicy:
    lp = 0
    def __init__(self):
        self.nazwisko = ""
        self.imie = ""
        self.dzial = ""
        self.kasa = 0
        self.idex_update = 0
        self.lp = 0

    def update_pracownika(self):
        print(f"Aktualizacja danych dla :{self.lp} | {self.nazwisko}")
        self.dzial = input("Nazwa działu: ")
        self.kasa = input("Nowe wynagrodzenie: ")
        return (self.dzial, self.kasa)

    def wydruk_pracownika(self):
        print(f"Lp.{self.lp}| {self.nazwisko} | {self.imie} | {self.dzial} | {self.kasa} zł netto")

    def wydruk_po_aktualizacji(self):
        print(f"Lp.{self.lp}| {self.nazwisko} | {self.imie} | {self.dzial} | {self.kasa} zł netto")

class NowyPracownik(Pracownicy):

    def add_pracownik(self):
        self.lp = input("Lp: ")
        self.nazwisko = input("Nazwisko: ")
        self.imie = input("Imie: ")
        self.dzial = input("Dzial: ")
        self.kasa = input("Kasa: ")
        self.tabela_dane = tabela_dane = []
        tabela_dane.append(self.nazwisko)
        return (self.lp, self.nazwisko, self.imie, self.dzial, self.kasa )



# nowy_pracownik = Pracownicy("Kowalski", "Roman", "Spawalnia", 3450)
pracownik_0 = NowyPracownik()
pracownik_0.add_pracownik()
pracownik_1 = pracownik_0
pracownik_1.wydruk_pracownika()
pracownik_1.update_pracownika()
pracownik_1.wydruk_po_aktualizacji()



