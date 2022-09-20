import random
tab1 = ["X", "*", ".",]
tab2 = []
a=0
while a < 30: #len(tab1)
    fields_file = open("fields.txt", "a")
    fields_file.readable()
    x = random.choices(tab1, k=5)
    print(x)
    '''tab2.append(x)
    print(tab2, "\n")'''
    fields_file.write(str(x))
    fields_file.close()
    '''print(x, end = "")
    print("\n")
    print(x, end="")
    print("\n")'''
    a += 1




