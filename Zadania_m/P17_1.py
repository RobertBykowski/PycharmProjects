# Program przechodzi po każdej parzystej liczbie z przedziału
# od 1-100. Jeśli liczba podzielna jest przez 6 spraw aby licznik
# powiększył się o 1. Na koniec wyświetl informację, ile liczb
# jest parzystych oraz ile jest podzielnych przez 6.

# The program runs after each even group in the interval
# 1-100. If the number is divisible by 6, make the numerator
# has increased by 1. Finally, information on how many numbers
# is even and how much is divided by 6.
ii = 0
for i in range(2, 100, 2):
    if i%6 == 0:
        ii += 1
print(f"Mamy {ii} liczb podzielnych przez 6 są one parzyste")


