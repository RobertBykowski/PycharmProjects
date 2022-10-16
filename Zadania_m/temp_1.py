import re
str = "Ola ma kota i psa"
match = re.search(r"psa", str)
if match:
    print ("found ",match.group())
else:
    print ("not found")

