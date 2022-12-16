# Tworzymy generator, który będzie mnożył podane liczby
def multiply_numbers(numbers):
    for number in numbers:
        yield number * 2

# Uruchamiamy generator i wyświetlamy wyniki
print(type(multiply_numbers(1)))
for result in multiply_numbers([1, 2, 3, 4, 5]):
    print(result)
