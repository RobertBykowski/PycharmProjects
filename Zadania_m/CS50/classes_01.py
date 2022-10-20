class English_words:

    no_of_words = 0

    def __init__(self, word, pl_meaning, verb, adj, s1):
        self.word = word
        self.pl_meaning = pl_meaning
        self.verb = verb
        self.adj =  adj
        self.s1 = s1

        English_words.no_of_words += 1

    def full(self):
        return '{} {}'.format(self.word, self.pl_meaning)

print(English_words.no_of_words)

word_1 = English_words("do", "robić", "do", "overdone","yes")
word_2 = English_words("make", "robić", "do", "unmade","yes")
word_3 = English_words("dress", "bierać się", "dress", " dressed","yes")

print(word_1.__dict__)
print(word_2.__dict__)
print(word_3.__dict__)
print(English_words.no_of_words)
