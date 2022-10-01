#input("Put name and family name no 1: ")/ ##input("Put name and family name no 2: ")

list_1 = ("Robert Bykowski")
list_2 = ("Adam Kowalski")
index_spac_1 = (list_1.find(" "))
index_spac_2 = (list_2.find(" "))
len_1 = len(list_1)
len_2 = len(list_2)

print(list_1[0:(len(list_1[0:index_spac_1])//2)]+list_2[0:(len(list_2[0:index_spac_2])//2)])


print("-------------------------")
print("Index spacji 1:",index_spac_1)
print("Długosc string 1:", len_1)
print("-------------------------")
print("Index spacji 2:",index_spac_2)
print("Długosc string 2:", len_2)








