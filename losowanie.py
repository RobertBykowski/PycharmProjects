import random

lista1 = []
for i in range(3):
    lista2 = [".", "*", "X"]
    #tu zawartość twoej pętli np kolejna pętla
    for i in range(1):
        #lista2.append(random.randint(1,3))
        random.shuffle(lista2)
        #print(lista2)
    #tutaj znowu przejdz do mojego kodu
    lista1.append(lista2*3)
for skladnik in lista1:
    print(skladnik)

