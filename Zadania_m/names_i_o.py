for i in range(3):
    wybor = input("Chcesz zagrać wpisćnij klawisz <t> jeśli nie klawisz <n> : ")
    while wybor == "t":
        cyfra = int(input("Podaj cyfrę 1-10"))
        if cyfra == 3:
            print("Wygrałeś")
            wybor = input("Chcesz zagrać wpisćnij klawisz <t> jeśli nie klawisz <n> : ")

    if wybor == "n":
        print("Wybrałeś <n>")
    else:
        print("Wybrałeś inną literę niż <t>")




