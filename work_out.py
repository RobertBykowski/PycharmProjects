# tab = ["ola", "ma", "kota"]
# for i in tab:
#     print(*i)
#
# for user in range(0, 3):
#     name = input("Jak masz na imię?")
#     print("Cześć", name)

# for i in range(0, 10):
#     print(*"wartosc:", i)

# list = ["Ala ma kota", "Kot ma Alę", "Oni mają psa"]
# for i in list:
#     print(i)

# for i in range(1):
#     for j in range(1, 9):
#         print(j * "#")
# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

# tab = [1,2,3,4,5,6,7,8,9,10]
# for i in tab:
#
#     for a in range(1,10):
#         a = i+(i-1)
#     print(a)


# for i in range(1):
#     for a in range(1,10):
#         b = a * a * a
#         print(b, end=" ")

1
2
3
4
5
6
7
8
9

namesList = str(input('Wprowadź listę imion używając przecinku lub spacji: '))

for i in namesList.split(' '):
   if i == ' ' or i == '':
      continue
   else:
      for j in i.split(','):
         print('Hi', j)







