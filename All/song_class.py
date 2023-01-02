class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_m_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "Nie chcę zostać pozwany",
                   "Więc tu zrobię przerwę"])
bull_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])

happy_bday.sing_m_a_song()
bull_on_parade.sing_m_a_song()

