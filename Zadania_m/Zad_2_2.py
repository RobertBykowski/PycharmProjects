# Napisz program, który automatycznie tworzy listę składającą się
# z następujących licz całkowitych: wartość początkowa listy wynosi 1,
# watość końcowa wynosi 10, wartość kolejnego przyrostu wynosi 2.
# Dodatkowo program oblicza długość sekwencji.
# -----
# Write a program that automatically creates a folding list
# of the following integers: the initial value of the list is 1,
# the final value is 10, and the value of the next increment is 2.
# Additionally, the program calculates the sequence length.
def main():
    numbers = list(range(1,10,2))
    print("Our generated list by function range is: ", numbers)
    print("A loop FOR for interacion via list.")
    for i in numbers:
        print(i)
    print("Access to the list by index")
    index = 0
    while index<len(numbers):
        print("numbers[", index,"] = ", numbers[index])
        index +=1
    print(len(numbers,))
main()
