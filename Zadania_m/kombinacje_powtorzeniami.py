#Kombinacje z powtórzeniami
#Rzucamy trzema kostkami do gry jednocześnie, ile jest możliwych wyników.
# k=3  - ilość elementów w zbiorze
# n=6  - ilość ścianek na kostce
# (n+k−1)!
#---------- =
# k!⋅(n−1)!
# 2 po potęgi 3 = 8 (2*2*2)

def silnia(n): return n*silnia(n-1) if n > 1 else 1

k = int(input("Podaj k :"))
n = int(input("Podaj n :"))

l = silnia(n+k-1)
m = silnia(k) * silnia(n-1)
wynik = l/m

print(int(wynik))