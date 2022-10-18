def oblicz(a):
    return a * a + 1

def main():
    step = 0.5
    x = 0
    while x <=5:
        y = oblicz(x)
        print(x,y)
        x += step
main()

