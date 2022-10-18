def trojka_pitago (a, b, c):
    if a * a + b * b == c * c:
        return "Tworzą trójkę"
    else:
        return "Nie tworzą trójki"

def main():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    print(trojka_pitago(a, b, c))
main()
