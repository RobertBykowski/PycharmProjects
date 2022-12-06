import math

class Dane:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h


    def __str__(self):
        pass

class Dzialania(Dane):
    def pole_trojkata(self):
        return (self.a * self.b * self.h)
    def pole_prostokata(self):
        return (self.a * self.b)
    def pole_kola(self):
        return (self.a * self.a) * (math.pi)
    def pole_trapezu(self):
        return (((self.a + self.b)/2) * self.h)



a = int(input("A: "))
b = int(input("B: "))
h = int(input("h: "))

w = Dane(a,b,h)
print(f"pole_trojkata = {Dzialania.pole_trojkata(w)}")
print(f"pole_prostokata = {Dzialania.pole_prostokata(w)}")
print(f"pole_kola = {Dzialania.pole_kola(w):.2f}")
print(f"pole_trapezu = {Dzialania.pole_trapezu(w)}")