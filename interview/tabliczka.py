tabliczka = []
rzad = []
for i in [(_) for _ in range(1,11)]:
    for j in [(_) for _ in range(1,11)]:
        rzad.append(i*j)
    tabliczka.append(rzad)
    rzad= []

for i in range(10):
    print(f"{tabliczka[i]}")
