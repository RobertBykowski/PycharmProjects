with open("slowa.txt") as plik:
    slowa = [i.split() for i in plik]
literaA = [i[0] for i in slowa if[0][-1] == "a"]
literaA += [i[0] for i in slowa if[1][-1] == "a"]

zawiera = [i[0] for i in slowa if i[0] in i[1]]
anagram = [i[0] for i in slowa if sorted(i[0]) == sorted(i[1])]

print(len(literaA), len(zawiera), len(anagram))