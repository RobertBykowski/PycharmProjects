# 1,1,2,2022-02-09
# id =13, uczen_id = 4, book_id = 8, data_wypozyczenia
import random
from datetime import date


randomuser = random.sample(range(1, 5), 4)
randombook = random.sample(range(1, 9), 4)
list_dt = []

for x in range(10):
    y = random.sample(range(2018, 2022), 1)
    m = random.sample(range(1, 12), 1)
    d = random.sample(range(1, 31), 1)
    x = str(date(*y, *m, *d))
    list_dt.append(x)

matrix = [
    [*randomuser],
    [*randombook],
    [*list_dt],
]
# lista2 = [[row[i] for row in matrix] for i in range(4)]
lista2 = list(zip(*matrix))
print(*lista2, sep=",\n")



