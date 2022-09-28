# Napisz program, który inicjalizuje zmienną o wartości 5 w celu
# przedstawienia liczby mil. Następnie przekonwertuj tę zwartość na kilometry,
# a potem na metry wykorzystując wzór km = mile/0,62137 oraz metry = 1000 km.
# Wyświetl wynik w następującej formie:
# mile
# 5
# km
# 8.04672
# metry
# 8046.72

miles = 5
km = miles / 0.62137
meters = 1000*km
print(f"{km:.5f}\n",f"{meters:.2f}")

# km = mile/mile_convert_float
# km_bis = int(km)
# m =km_bis/1000
# print("mile", mile)
# print("km", km)
# print("metry", km_bis)

