dic = {
    "PL" : "Polska",
    "DE" : "Niemcy",
    "RU" : "Rosja"
}
list_ = [ ]
while True:
    choice = input("Put a key : ")

    if choice in dic:
        key = dic.get(choice)
        list_.append(key)
        # print(key)
        continue
    if choice == "q":
        print("Koniec wyboru")
        break
    else:
        print("Wrong, try again")
        continue

print("Kolejny blok kodu")
print(list_)