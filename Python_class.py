'''
#if statments
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall meal") # jeśli oba warunki są True
elif is_male and not(is_tall):
    print("You are a short meal") #jeśli warunek is_tall is False
elif not(is_male) and is_tall:
    print("You are not a meal but tall")
else:
    print("You are either not male or not tall or both") # obwa warunki są False
    '''
'''
#if Statements nad Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif  num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(1,8,3)) 
'''
'''
#Building a Better Calculator
num1 = float(input("Enter a first number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter a second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1 / num2)
elif op == "-":
    print(num1 * num2)
else:
    print("Invalid operator")
    '''
'''
#Dictionaries
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
}
print(monthConversions.get("Jan") +" "+ "Feb")
'''
#While loop
'''i = 1
while i <= 10:
    print(i)
    i = i + 1 # you can also write it down on that way i += 1
print("Done with loop")'''

'''list = (1, 2, "Alice", "Home", 3, 4)
for i in list:
    print (i, "This loop for")'''

'''list = ("home", "dog", "forest")
i = input("Put word: ")
while i == "dog":
    print(i)
print("This world is not dog")'''

'''secret_word = input("Set up your secret word: ")
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Put guess: ")
        guess_count += 1
        guess_count_limit = guess_limit - guess_count
        print("That was your guess no.", guess_count,
              " !!! Only", guess_count_limit,"guesses left")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You limit of guesses is up")
else:
    print("You win!")'''
#For loop
'''friends = ["Jim", "Julia", "Robert"]
for friend in friends:
    print(friend)
    
for index in range(2,10):
    print(index)'''

'''friends = ["Jim", "Julia", "Robert"]
for index in range(len(friends)):
    print(friends[index])'''
# Reading files
'''employee_file = open("employees.txt")
#print(employee_file.readable()) #sprawdza czy plik jest czytany
#print(employee_file.read())
print(employee_file.readlines()[0])
employee_file.close()'''

'''employee_file = open("employees.txt")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()'''
#Dopisywanie do pilku
employee_file = open("employees.txt", "a") #"w" nadpiszesz plik
employee_file.write("\n9.Wycieczka anulowana")
employee_file.close()











