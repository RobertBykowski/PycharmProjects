#rozwiązanie imperatywne
# def fibonacci (n, first = 0, second = 1):
#     for _ in range(n):
#         print(first, ", ", end = "", sep ="")
#         first, second = second, first + second
# def main():
#     fibonacci(30)
# main()

#rowiązanie funkcyjne
def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
def main():
    for n in range(10):
        print(fibonacci(n),", ", end = "", sep ="")
main()
