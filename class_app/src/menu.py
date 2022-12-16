# menu.py
from record import Record
from database import Database

def show_menu():
    while True:
        print("Menu:")
        print("1. Add record")
        print("2. Remove record")
        print("3. Edit record")
        print("4. Find record")
        print("5. Display record")
        print("6. Quit")

        choice = input("Enter your choice: ")
        if choice == '1': #Add record
            print("Wybrałeś 1")
        elif choice == '2': #Remove record
            pass
        elif choice == '3': #Edit record
            pass
        elif choice == '4': #Find record
            pass
        elif choice == '5': #Display record
            pass
        elif choice == '6': #Quit
            return
        else:
            print("Invalid choice. Try again.")

