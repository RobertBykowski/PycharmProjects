#https://docs.python.org/pl/3/tutorial/datastructures.html

import itertools
import pandas as pd
a = []
lista_nazw_kolumn = []
list_ = ["T","N"]
no_reapeat = int(input("Podaj ilość warunków :"))
ilosc_kolumn_p = 2 ** no_reapeat

for i in range(1,ilosc_kolumn_p + 1):
    lista_nazw_kolumn.append("P" + str(i))
warunki = []
for j in range(1, no_reapeat + 1):
    warunek = input(f"Podaj warunerk nr {j}: ")
    warunki.append(warunek)
print()
for v in itertools.product(list_, repeat=no_reapeat):
    a.append(v)
q = list(zip(*a))
df_a = pd.DataFrame(q)
df_a.columns = lista_nazw_kolumn
df_a.insert(0, "Warunki", warunki)

print(df_a)





