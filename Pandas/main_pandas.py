import csv

with open("list_of_names.csv") as data_file:
    data= csv.reader(data_file)
    nazwisko = []
    for row in data:
        if row[1] != "Nazwisko":
            nazwisko.append(row[1])
    print(*nazwisko)