


def znajdz_wzorzec(text, wzorzec):
    liczba_wystapien = 0
    dl1 = len(text)
    dl2 = len(wzorzec)


    for i in range (dl1-dl2+1):
        if text [i] == wzorzec[0]:
            if text [i:i+dl2] == wzorzec:
                print(f"Znaleziono wzorzec {wzorzec} na pozycji {i}")
                liczba_wystapien += 1
    if liczba_wystapien == 0:
        print(f"Nie znaleziono wzoraca {wzorzec}")
    else:
        print(f"Wzorzec {wzorzec} w tekście występuje {liczba_wystapien} razy")

with open("email_ANSI.txt", mode = 'r', encoding='cp1250') as f:
    tekst = f.read()
    print(tekst)
znajdz_wzorzec(tekst, ".pl")







