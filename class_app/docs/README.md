# Program ma tworzyć mini baze danych: Imie, Nazwisko, nr telefonu.
# - dane przechowyane w słowniku
# - pole telefon - 9 cyfr w formacie (xxx-xxx-xxx)
# Funkcjonalności: dodawanie, usuwanie, edycja, wyszukiwanie, wyświetlanie.

# dodawaie do słownika
    - Dodawanie nowego elementu do słownika
    - people['Charlie'] = 35
    - people.update({'Charlie': 35, 'Eve': 28})

# usuwanie ze słownika
    - del people['Alice']

# edycja rekodu słownika
    - Nadpisywanie wartości istniejącego elementu
    - people['Alice'] = 26

# wyświetlanie:
# całego słownika,
    - Wyświetlenie słownika za pomocą operatora %
    - print('%s' % people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
    - Sortowanie elementów słownika według wartości
    - sorted_by_value = sorted(people.items(), key=lambda x: x[1])
    - print(sorted_by_value)

# wyszukiwanie i wyświetlenie pojedynczego rekordu
    value = dictionary.get('Alice')
    if value:
        print(value)
    else:
        print('Klucz nie został znaleziony w słowniku.')