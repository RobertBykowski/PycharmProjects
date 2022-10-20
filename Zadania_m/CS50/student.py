def main():
    student = get_student()
    print(student)
    print(f"{student[0]} from {student[1]} has a {student[2]}")


def get_student():
    name = input("Name : ")
    house =  input("House : ")
    car = input("Car : ")
    return [name, house, car]

if __name__ == "__main__":
    main()
