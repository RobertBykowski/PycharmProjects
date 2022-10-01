secret = "kod"
guess = input("Zgadznij, jakie to słowo: ")
tries = 1
while guess != secret:
    print("Do tej pory próbowałeś", tries,"razy")
    guess = input("Spróbuj ponownie podaj słowo: ")
    tries +=1
    if tries == 5:
        print("Próba", tries, " była twoją ostatnią <Game over>")
        break
print("Udało się zgadłeś słowo", guess)