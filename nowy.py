# s = "ab12c59p7dq"
# digits = []
# for symbol in s:
#     if "1234567890".find(symbol) != -1:
#         digits.append(int(symbol))
#         print(symbol)
# print(digits)

data = ["10,537.4", "$", "1,086.0", "$", "291.1", "$", "465.3", "$", "12,379.8"]

result = []
pos = 0 

while True:
    try:
        pos = data.index("$", pos)
    except ValueError:
        break

    result.append(pos)
    pos += 1 # zacznij jedno miejsce za ostatnio znalezionym

print(result)
