import random
import string
alphabet = list(string.ascii_letters) + list(string.hexdigits) + list(string.octdigits) + list(string.punctuation)
no_characters = int(input("Podaj ilość znaków w haśle: "))
password = ""
for j in range(10):
    for i in range(1, no_characters + 1):
        password += random.choice(alphabet)
    print(password)
    password = ""
 





