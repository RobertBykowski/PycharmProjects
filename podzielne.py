lista_podzielne = []
lista_nie_podzielne = []
for i in range(1,21):
    if i % 3 != 0:
        lista_nie_podzielne.extend([i])

    else:
        lista_podzielne.append([i])


print ("Nie podzielne przez 3 >>\n", f'{lista_nie_podzielne}')
print("Podzielne przez 3 >>\n", lista_podzielne)