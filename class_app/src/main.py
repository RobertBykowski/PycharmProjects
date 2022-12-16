from record import Record
from database import Database
from validation import is_valid_phone_number
import menu

menu.show_menu()


first_name = input("Enter your name: ")
last_name = input("Enter the name: ")
phone_number = input("Enter your phone number (XXX-XXX-XXX): ")

# Validate the phone number
if is_valid_phone_number(phone_number):
    # If the phone number is valid, create the record
    record = Record(first_name, last_name, phone_number)


else:
    # If the phone number is not valid, display an error message
    print("Error: Invalid phone number format")

record_dict = record.to_dict()
print("-------------------------------")
Database.display_record(record_dict)
