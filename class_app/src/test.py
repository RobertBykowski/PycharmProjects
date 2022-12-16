from menu import show_menu

class Dane:

    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def wyswietl(self):
        for obj in lista:
            print(f" {obj.imie} {obj.nazwisko} {obj.telefon}")

lista = []
for _ in range(2):
    osoba = Dane(imie=input("Podaj imie: "), nazwisko=input("Podaj nazwisko: "),
                 telefon=input("Podaj telefon: "))
    lista.append(osoba)

Dane.wyswietl(lista)


imie = input("Podaj imię do wyszukania: ")
for obj in lista:
    if obj.imie == imie:
        print(f"Mamy to {obj.imie} {obj.nazwisko} {obj.telefon}")
        obj.imie = input("Podaj nowe imię:")
        print(f"Nowe dane {obj.imie} {obj.nazwisko} {obj.telefon}")
    else:
        continue


