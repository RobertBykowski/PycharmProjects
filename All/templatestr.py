
# name = input("Write your name: ")
# family_name = input("Write your family name: ")
# print("Twoje imie to"+name)
# print("Twoje nazwisko to "+family_name)

# List - how to creat list
#friends = ["Kevin", "Karen", "Tom"]
#              0       1        3   Negative value -1
#print(friends[0])
#print(friends[1:2])
# Change one element of this list
#friends[1] = "Mike"
#print(friends)

# List funkcions
lucky_numbers = [4, 8, 9, 10, 56]
friends = ["Kevin", "Karen", "Tom", "Ala", "Bob"]
#friends.extend(lucky_numbers) #Extend your list on this way
# friends.append("Julia") # Add one element to list
#name = input("Write your name: ")
#new_friend = friends.insert(3,(name))
# result ['Kevin', 'Karen', 'Tom', 'Olga']
# print(friends.index("Tom")) # It gives index of one element from list. Method - index
# print (friends.sort()) Method - sort
#print(friends)

#Tuples - kontener gdzie gromdzimy zmienne - krotka (struktura danych)
#coordinates = [(4,5), (7,8), (12,56,"Home")]
#print(coordinates[2])

#Functions
#def say_hi(name, age):
#   print("Hello user " + name +  "\nYour age is " + age)
#name = input("Let me ask about your name: ")
#age = input("Let me ask about your age: ")
#say_hi(name, age)

#Return Statement (Komunikat zwracający)
def cube(num, num2):
    return num**num2

num = input("Podaj liczbe : ")
num = int(num)
num2 = input("Podaj drugą liczbe : ")
num2 = int(num)

result = cube(num, num2)
print("--------------------------------------------")
print("Liczba", num, "do potęgi", num2, "= ", (result))





