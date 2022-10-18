def dodawanie(a, b):
    c = a + b if a > 0 else "A musi być większe od zera"
    return c
def main():
    a = int(input("a : "))
    b = int(input("b : "))

    print(dodawanie(a, b))

main()

