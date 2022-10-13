def list_unique_names(phonebook):
    unique_names = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ",1)
        for unique in unique_names:
            if unique == first_name:
                break
            else:
                unique_names.append(first_name)
    return len(unique_names)

def set_unique_names(phonebook):
    unique_names = set()
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ",1)
        unique_names.add(first_name)
    return len(unique_names)
phonebook = [
    ("Jan Nowak", "555-555-5555"),
    ("Adam Adamiec", "555-222-5555"),
    ("Jan Kowalski", "444-555-5555"),
    ("Albert Nowakowski", "111-555-5555"),
    ("Albercik Frankowski", "111-555-5555"),

]
print("Liczba unikalnych imion, metoda zbiór",
set_unique_names(phonebook))

print("Liczba unikalnych imion, metoda list",
list_unique_names(phonebook))