# Funkcje rekurencyjne możemy wykorzystać do
# obliczeń lub wypisywania pewnych informacji
# na ekranie. Często mają one krótszą postać
# niż analogiczne rozwiązania iteracyjne.
# Jednak zwykle zajmują więcej pamięci
# komputera na przechowywanie potrzebnych
# danych i działają wolniej.

lista = [1,2,3,4]
# def suma(lista):
#     suma = 0
#     for x in lista:
#         suma += x
#     return suma
#
# l = suma(lista)
# print(l)

# def suma(lista):
#     # przypadek bazowy
#     if lista == []:
#         return 0
#     # przypadek rekurencyjny
#     else:
#         return lista[0] + suma(lista[1:])
#
# lista = [1,2,3,4]
# print(suma(lista))
#
# def sum(liczba):
#     if liczba == 0:
#         return 0
#     else:
#         return liczba + sum(liczba-1)
#
# print(sum(2))

from turtle import *

def kw():
    for i in range(4):
        fd(20); lt(90)

def pasek(n):
    if n > 0:
        kw(); fd(20)
        pasek(n-1)

tracer(0)
pasek(5)
update()