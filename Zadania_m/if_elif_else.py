gretting = input("Say hello in English or Spanish : ")
greet_en = ("hi", "Hi", "hello", "Hello")
greet_sp = ("hola", "Hola")
if gretting not in greet_en and gretting not in greet_sp:
    print("I don't know what you say")
elif gretting in greet_en:
    num = int(input("Put on 1 or 2: "))
    print("You are speking in English")
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
elif gretting in greet_sp:
    num = int(input("Put on 1 or 2: "))
    print("You are speking in Spanish")
    if num == 1:
        print("uno")
    elif num == 2:
        print("dos")
