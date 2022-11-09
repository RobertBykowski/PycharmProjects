# Napisz program, który dla wczytanej od użytkownika
# liczby całkowitej będącej numerem dnia tygodnia
# (0 – niedziela, 1 – poniedziałek, … , 6 – sobota)
# wyświetli godziny pracy urzędu w tym dniu, lub informację,
# że urząd jest nieczynny, według poniższych informacji.
# Dla niepoprawnych  danych należy wyświetlić komunikat o błędzie danych wejściowych.
# Godziny pracy urzędu:
# Pn: 10-14
# Wt: 10-19
# Śr-Pt: 11-16
# So-Nd: Nieczynne

godz_prac = ["Nieczynne","10-14","10-19","11-16","11-16","11-16","Nieczynne"]
while True:
    try:
        dzien = int(input("Podaj dzien tygodznia (0-9): "))
        print(godz_prac[dzien])
        break
    except IndexError:
        print("Oops!  That was no valid number.  Try again...")


