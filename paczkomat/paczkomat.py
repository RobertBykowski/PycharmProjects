class Box:

    def __init__(self):
        print()

    def czytaj_wymiary(self):
        self.height = int(input("Podaj wys: "))
        self.width = int(input("Podaj sz: "))
        self.length = int(input("Podaj dl: "))

    def spr(self):
        if self.height < 2 and self.height < 8:
            print("Wymiar A poza zakresem")
            if self.width <= 38:
                print("Wymiar B poza zakresem")
                if self.length <= 64:
                    print("Wymiar C poza zakresem")

    def wyswietle_wymiary(self):
        print(f"Wysokość {self.height}|{self.width}|{self.length}")


pudlo=Box()
pudlo.czytaj_wymiary()

pudlo.wyswietle_wymiary()







