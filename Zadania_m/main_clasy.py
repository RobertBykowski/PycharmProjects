# Ćwiczenie 1: Należy utworzyć klasę książka. Klasa, powinna:

# Przechować informacje na temat: tytułu, ilości stron, autora, data wydania, właściciel
# Posiadać 2 metody / funkcje
# 1 – zwraca informacje na temat książki,
# 2 – zmianę właściciela książki
# Ćwiczenie 2: korzystając z wyżej zdefiniowanej klasy, utworzyć kilka obiektów
# klasy książka, po czym dodać je do listy książek. Lista książek, to zwykła
# zmienna typu 'lista’.



class Book(object):

    def __init__(self, title, page_no, writer, bound_book_date, owner):
        self.title = title
        self.page_no = page_no
        self.writer = writer
        self.bound_book_date = bound_book_date
        self.owner = owner

# funkcja – 1 – zwraca informacje na temat książki,
    def book_info(self):
        print(self.title)
        print(self.page_no)
        print(self.writer)
        print(self.bound_book_date)
        print(self.owner)

# funkcja 2 – zmianę właściciela książki
    def change_owner(self, newOwner):
        self.owner = newOwner


book_1 = Book("Pan Tadeusz", 340, "Mickiewicz", 1834, "Malinowski" )
book_2 = Book("Zbrodnia i kara", 30, "Dostojewski", 1734, "Makowski" )
book_3 = Book("Potop", 49, "Sienkiewicz", 1934, "Niemcewicz" )
book_4 = Book("Dżuma", 140, "Camus ", 1984, "Nowak" )
list = [ book_1, book_2, book_3, book_4 ]
def show_list():
    for i in list:
         print(f"{i.owner}, {i.title}")

show_list()