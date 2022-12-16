# plik zawierający klasę reprezentującą pojedynczy rekord bazy danych.
#     Klasa "Record" atrybuty jak:
#     "first_name",
#     "last_name",
#     "phone_number"

class Record:

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def to_dict(self):
        return {
        'key': [ self.first_name, self.last_name, self.phone_number ]
    }







