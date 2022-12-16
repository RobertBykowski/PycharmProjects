from record import Record
from database import Database
from validation import is_valid_phone_number
import menu
for _ in range(3):
    first_name = input("Enter your name: ")
    last_name = input("Enter the name: ")
    phone_number = input("Enter your phone number (XXX-XXX-XXX): ")
    record = Record(first_name, last_name, phone_number)
    record_dict = record.to_dict()
    choice = input("Enter your choice: ")


print("-------------------------------")
Database.display_record(record_dict)