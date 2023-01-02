# a = 10
# b = 5
# operacja = input("Podaj działanie: (+) (-): ")
# wynik = a + b if operacja == "+" else a - b
# print("Wynik=", wynik)
# -------------------------------
# name1 = input("Enter name 1: ")
# name2 = input("Enter name 2: ")
#
# print("Names are same.") if name1 == name2 else print("Names are differnt.")
# -----------------------------------------------
import random
numbers = 2
suma = 0
min = random.randint(0,100)
print(min)
max = min
suma += min
for i in range(numbers-1):
    liczba = random.randint(0,100)
    print(liczba)
    if max < liczba:
        max = liczba
    if liczba < min:
        min = liczba
    suma += liczba
print("Najw", max)
print("Najm", min)
print("Sred", suma/numbers)


