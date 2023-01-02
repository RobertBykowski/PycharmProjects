class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line, end=" ")

happy_bday = Song(["Happy birthday to you",
                   "Nie chce zosta? pozwany",
                   "Wi?c tutaj przerw?"])
blue_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])

dane = Song(["Ona", "On", "Ono"])
lista = "Ala ma kota"
dane1 = Song(lista)
dane1.sing_me_a_song()
