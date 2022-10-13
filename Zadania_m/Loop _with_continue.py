x = 0
for x in range(20):
    print("x to", x)
    if x < 5:
        continue
    print("x jest większe od 5")
    if x % 10 == 0:
        continue
    print("x nie dzieli się przez zero!")
    if x != 2 and x != 4 and x != 16 and x != 32 and x != 64:
        continue
    print("x jest potęgą 2")