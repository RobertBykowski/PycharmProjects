def f(x): return x % 2 != 0 and x % 3 != 0 # funkcja filtrująca
def main():
    first = list(filter(f, range(10,25)))
    print("Liczby pierwsze", first)
main()
