
# # s = "ab12c59p7dq"
# # digits = []
# # for symbol in s:
# #     if "1234567890".find(symbol) != -1:
# #         digits.append(int(symbol))
# #         print(symbol)
# # print(digits)
#
# # data = ["10,537.4", "$", "1,086.0", "$", "291.1", "$", "465.3", "$", "12,379.8"]
# #
# # result = []
# # pos = 0
# #
# # while True:
# #     try:
# #         pos = data.index("$", pos)
# #     except ValueError:
# #         break
# #
# #     result.append(pos)
# #     pos += 1 # zacznij jedno miejsce za ostatnio znalezionym
# #
# # print(result)
#
# sentence = "Google /Cloud/Platform/lets, you build, deploy"
# a1 = sentence.split("/")
# print(a1)
#
# str1 = "27-12-2016"
# a = str1.split("-")
# print(a)

import re

# m = re.search("(?<=abc)def", "abcdef")
#
# m.group(0)
# tekst = "<?user@host.com"
# x = re.match(r"(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)", tekst)
# print(str(x))


import re

phone_no = "       'n', '3               kontakt@momentumway.com"

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.com"
pattern = "['a-z']+['0-9']"
result = re.sub(pattern, "", phone_no).strip()
print(f" ,{phone_no}")
print(result)
