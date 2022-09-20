tablica1 = []
tablica2 = ("X", "*", ".")
n = 0
a = ""
while(n<1): #warunek
    n=n+1
    for a in tablica2:
        tablica1.append(a)
        print(tablica1, end="")
        fields_file = open("fields.txt", "a")
        fields_file.readable()
        # znak_bis = map(lambda x: x + "\n", tablica1)
        # fields_file.writelines(znak_bis)
        fields_file.write(str(tablica1))
        fields_file.close()
