# The program checks whether the numbers a, b,
# and c make up the Pythagorean triple.
# ang. conditional operator

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
c = int(input("Enter number c : "))

if a * a + b * b == c * c:
    print(f"Numbers:{a},{b},{c} create the Pythagorean triple")
else:
    print(f"Numbers:{a},{b},{c} do NOT create the Pythagorean triple")
