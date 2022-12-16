Oto kilka ogólnych wskazówek dotyczących struktury i nazewnictwa plików w projekcie Python:

[//]: # (README.md: )
    plik tekstowy zawierający wprowadzenie do projektu, instrukcje instalacji i informacje ogólne.
    
    LICENSE: plik z informacjami o licencji, na jakiej udostępniono projekt.
    
    setup.py: plik zawierający instrukcje instalacji i konfiguracji projektu.
    
    requirements.txt: plik z listą zależności (bibliotek i narzędzi) wymaganych do działania projektu.
    
    .gitignore: plik zawierający listę plików i katalogów, które nie powinny być uwzględniane w kontroli wersji (np. pliki binarne, pliki tymczasowe itp.).
    
    src/: katalog zawierający kod źródłowy projektu.
    
    tests/: katalog zawierający testy jednostkowe i integracyjne projektu.
    
    docs/: katalog zawierający dokumentację projektu.

--------------------------
 struktura plików będzie następująca:

# main.py: 
    plik główny programu, zawierający kod odpowiedzialny za uruchomienie 
    aplikacji i wywoływanie poszczególnych funkcjonalności

# database.py:
    plik zawierający klasę odpowiedzialną za przechowywanie i zarządzanie 
    bazą danych. Klasa ta mogłaby np. nazywać się "Database" i posiadać metody 
    takie jak:
    "add_record", 
    "remove_record", 
    "edit_record", 
    "find_record", 
    "display_records"
    
# record.py: 
    plik zawierający klasę reprezentującą pojedynczy rekord bazy danych. 
    Klasa ta mogłaby np. nazywać się "Record" i posiadać atrybuty takie 
    jak:
    "first_name", 
    "last_name", 
    "phone_number"