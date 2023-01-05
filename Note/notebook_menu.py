import sys
import add_new_note

while True:
    print("--- Mini-menu ---")
    print("1. New note")
    print("2. Edit")
    print("3. Find")
    print("4. Delete")
    print("5. Exit")
    print("-----------------")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print ("creating a new note")
        add_new_note.add_note()

    elif choice == 2:
        print("editing a note")

    elif choice == 3:
        print("finding a note")

    elif choice == 4:
        print("deleting a note")

    elif choice == 5:
        print("Exiting the program...")
        sys.exit()
    else:
        print("Invalid choice")