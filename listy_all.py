# #Tworzenie listy sposoby
# lista_zero = [] # pusta lista
#
# lista = [(i*1) for i in range(5)]
# print(lista)
#
# zdanie = "Ola ma kota i psa i mieszka w domu"
# lista_s = zdanie.split()
# print(lista_s)
#
# #iterowanie listy
# for i in lista_s:
#     print(i, end="-")
#
# print("")
# lista_nazwiska = ["Kowalski", "Nowak", "Kowalski"]
# for nazwisko in lista_nazwiska:
#     print(nazwisko, end="-")
#
# print()
# print(lista_nazwiska[0])
#
# # Create 2 independent lists
# list_1 = ["a","b","c"]
# list_2 = ["d","e","f"]
#
# # Create an empty list
# list = []
#
# # Create List of lists
# list.append(list_1)
# list.append(list_2)
# print (list)
#
# list = []
#
# # Create List of list
# for i in range(5):
#     list.append([])
#     for j in range(5):
#         list[i].append(j)
#
# print(list)

subject = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s ś t u v w x y z ź ż"
verb = "0 1 2 3 4 5 6 7 8 9"
object = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s ś t u v w x y z ź ż"
manner  = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s ś t u v w x y z ź ż"
palce = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s ś t u v w x y z ź ż"
time = "a ą b c ć d e ę f g h i j k l ł m n ń o ó p q r s ś t u v w x y z ź ż"

import random
def zamiana(text):
    l = text.split()
    lista = list(l)
    return lista

lista_list =[]
top = [subject, verb, object, manner, palce, time] #
for i in top:
    lista_list.append(zamiana(i))

xlist = []
for x in range(6):
    rc = random.choice(lista_list[x])
    xlist.append(rc)

print(*xlist)

