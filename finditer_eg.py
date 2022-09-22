import re
print(len("omnibus@pozyskajklientapl"))
target_str = "Ala ma kota omnibus@pozyskajklienta.pl i @psa i dom"
#target_str = "Jessa salary is 8000$ She is Python developer"
#pattern = r'"@"'
#replacement = r'"at"'
#result = re.sub(pattern, replacement, target_str)
#result = re.findall(r"\b\W\w{1}\b", target_str)
result = re.findall(r"\Bmnibus@", target_str)
#result = re.findall(r"[@][pl]", target_str) #Match Match p or y or t followed by either h or s./Dopasuj Dopasuj p, y lub t, a następnie h lub s.
print(result)







'''res = re.findall(r"\b\w{5}\b", "Jessa nad Kelly")
print(res)

import re

target_str = "Jessa is a Python developer, and her salary is 8000"

# \A to match at the start of a string
# match word starts with capital letter
result = re.findall(r"\A([A-Z].*?)\s", target_str)
print("Matching value", result)
# Output ['Jessa']

# \Z to match at the end of a string
# match number at the end of the string
result = re.findall(r"\d.*?\Z", target_str)
print("Matching value", result)
# Output ['8000']'''

