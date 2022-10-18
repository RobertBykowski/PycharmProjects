# def wiadomosc (i):
#     if i > 0:
#         print("To jest fukcja rekurencyjna")
#         wiadomosc(i - 1)
# def main():
#     wiadomosc(5)
# main()

def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x-1)

print(silnia(3))

