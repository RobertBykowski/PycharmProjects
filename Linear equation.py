# Linear equation ax + b = c
print("This code run a linear equation: ax + b = c")
a = float(input("Enter a: "))
if a == 0:
    print("Unacceptable value.", a)
else:
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    x = (c-b)/a
    print("Answer is")
    print(f"For {a}x + {b} = {c}, x = {x:.2f}")