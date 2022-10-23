class Cookie:
    def __init__(self, name, shape, chips='Chocolate'):
            self.name = name
            self.shape = shape
            self.chips = chips
    def bake(self):
        print(f'This {self.name}, is being baked with the shape {self.shape} and chips of {self.chips}')
        print('Enjoy your cookie!')
class Italian_cookie(Cookie):
    pass

cookie2 = Italian_cookie('Awesome cookie', 'Star')
cookie3 = Cookie('Well cooked', 'Oval')

cookie2.bake()