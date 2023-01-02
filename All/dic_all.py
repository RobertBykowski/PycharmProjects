# pusty słownik dane ={}
dane = {
        "Name" : "Ron",
        "F_name" : "Nowakowski",
        }
dane["ID"] = 123
dane["City"] = "Tokyo"
# z listy >> słownik
lista_dane = [["Cod_adress",87100],["Tel_no", "508351344"]]
dane_1 = dict(lista_dane)
# print(dane_1)
dane.update(lista_dane)
# print(dane["City"])
# print(dane.items())   # wyświetlenie wszystkich elementów słownika: par klucz - wartość
# print(dane.keys())    # wyświetlenie wszystkich kluczy słownika
# print(dane.values())  # wyświetlenie wszystkich wartości słownika

# tab =[print(key, dane[key]) for key in dane]

for item in dane.items():
    print(item)

for key, value in dane.items():
        print(key, '->', value)