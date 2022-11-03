# from itertools import combinations
# from itertools import combinations_with_replacement
# c = list(combinations_with_replacement(["Adam", "Bob", "Chris", "Don", "Tom"],2))
# print(c,".", end="")

text = "120 00 zł"
def zamiana(zmienna):
    return zmienna.replace(" ","").replace("zł","").capitalize()
l = text.replace(" ","").replace("zł","").capitalize()

print(l)
