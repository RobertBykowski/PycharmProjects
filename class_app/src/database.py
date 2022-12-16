# plik zawierający klasę odpowiedzialną za przechowywanie i zarządzanie
#     bazą danych. "Database" i posiadać metody
#     takie jak:
#     "add_record",
#     "remove_record",
#     "edit_record",
#     "find_record",
#     "display_records"
from record import Record

class Database:

    def add_record(self):
       pass
    # usuwanie ze słownika - del people[ 'Alice' ]
    @staticmethod
    def remove_record(record_dict):
        del record_dict[""]
        pass

    def edit_record(self):
        pass

    def find_record(self):
        pass

    @staticmethod
    def display_record(record_dict):
        for key, value in record_dict.items():
            print(f'{key}: {value}')
        # print (f"{record_dict.items}")





