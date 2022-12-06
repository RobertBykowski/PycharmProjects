import math
menu = {
        "bigMac" : 20.00,
        "mcChicken" : 23.00,
        "mcWrap" : 24.00,
        "mcZestaw" : 35.00,
        "coca-Cola" : 8.00,
        "woda" : 5.00,
        "sok" : 12.00
}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: { value:.2f} zł")
print("------------------------")

choice = ''
basket =[]
order =[]

choice = input("Select something from the menu : ")

for choice in menu.keys():
    key = menu.get(choice)
    basket.append(key)
    order.append(choice)

# ----------------
print()
print("---- Paragon nr 2345 ----")

for f, b in zip(order, basket):
        print(f"{f:10} {b:3.2f} zł")
total = math.fsum(basket)
print("-------------------------")
print(f"Do zapłaty {total:.2f} zł")

