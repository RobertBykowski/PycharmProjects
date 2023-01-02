import random
import linecache
tab1 = ["X", "*", ".",]
tab2 = []
a=0
while a < 30: #len(tab1
    x = random.choices(tab1, k=30)
    print(x)
    fields_file = open("fields.txt", "a")
    fields_file.readable()
    tab2.append(x)
    print("Nowa tablica ",tab2, "\n")
    fields_file.write(str(tab2))
    fields_file.close()
    '''print(x, end = "")
    print("\n")
    print(x, end="")
    print("\n")'''
    a += 1




