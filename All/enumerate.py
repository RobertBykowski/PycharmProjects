# pracownicy = ["Tom", "Ali", "Rob", "Bob"]
# for i, imiona in enumerate(pracownicy):
#     print(f"{i+1} {imiona}")

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError ("Missing name")
        if house not in [("Warszawa", "Toruń")]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} form {student.house}")

def get_student():
    name = input("Enetr student: ")
    house = input("Enter house : ")
    return Student(name, house)


if __name__ == "__main__":
    main()