# https://bulldogjob.pl/readme/co-musisz-wiedziec-zanim-uzyjesz-funkcji-zip-w-pythonie
# matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print(matrix[0][2])
# print(matrix[1][0])
# matrix_T = [list(i) for i in zip(*matrix)]
# print(matrix_T)
# def list_transform (list_):
#     l = list_.split()
#     ll = list(l)
#     return ll
#
#
# list1 =  "Ala Ola Mama Tom"
# list2 = "dom piec kot samochód"
#
# record = zip(list_transform(list1), list_transform(list2))
# print(list(record))

# names = ["Chandler", "Monica", "Ross", "Rachel", "Joey", "Phoebe"]
#
# zippedObject = zip(names)
# print("Converting zipped object into a list - ", list(zippedObject))
# ----------------------------------
# l1 = [(i) for i in range(1000)]
# l2 = [(i) for i  in range(60,2000)]
#
# for a, b in zip(l1, l2):
#     c = a + b
#     print(f" {c}={a}+{b}")
import operator
lista1 = [1,2,3,4]
lista2 = [2,3,4,5]
# for a, b in zip(lista1, lista2):
#     print(a*b, end=" ")
#
# a = list(map(operator.mul, lista1, lista2))
# print(a)
c = operator.sub(59,45)
print(c)
