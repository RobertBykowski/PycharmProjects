class Polonez(): # obiekt
    def hamuje(self):  # metoda
        return "Hamowanie"
    def cofa(self , predkosc): # metoda
        return f"Cofanie z prędkością {predkosc} km/h"
    def skreca(self, kierunek_skretu): # metoda
        return f"Skręca w {kierunek_skretu}."
    def dodawanie(self, a, b):
        return (a+b)

moj_polzonez = Polonez() # instancja klasy
print(moj_polzonez.hamuje())
print(moj_polzonez.cofa(10))
print(moj_polzonez.skreca("lewo"))
print(moj_polzonez.dodawanie(2,4))