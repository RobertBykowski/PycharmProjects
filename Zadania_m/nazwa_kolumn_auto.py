# lista_nazw_kolumn = []
no_reapeat = int(input("Podaj ilość warunków :"))
# ilosc_kolumn_p = 2 ** no_reapeat
# for i in range(1,ilosc_kolumn_p + 1):
#     lista_nazw_kolumn.append("P" + str(i))
# print(lista_nazw_kolumn)
warunki = [ ]
for j in range(1, no_reapeat + 1):
    warunek = input(f"Podaj warunerk nr {j}: ")
    warunki.append(warunek)
print(warunki)
