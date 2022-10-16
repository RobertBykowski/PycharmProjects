# import random
# list = []
#
# for i in range(0,5):
#     number = random.randint(0,100)
#     list.append(number)
#
# print(list)
# print(min(list),max(list))
# print(sum(list)/5)
# ---------------------
al = []
for i in range(65,91):
    alfabet = chr(i)
    al = alfabet.split(" ")
    reversed_list = al[::-1] # Syntax: reversed_list = systems[start:stop:step]
    print(reversed_list, end="")

