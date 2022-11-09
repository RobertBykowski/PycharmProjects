import random
import datetime


list_dt = []
for x in range(6):
    y = random.sample(range(2018, 2022), 1)
    m = random.sample(range(1, 12), 1)
    d = random.sample(range(1, 31), 1)
    x = datetime.date(*y, *m, *d)
    list_dt.append(x)
print(*list_dt, sep=", ")