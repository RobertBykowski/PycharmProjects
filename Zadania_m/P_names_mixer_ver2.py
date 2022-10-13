
def spplit(name):
    # name = "Nowakowski"
    list_name = []
    list_name1 = []
    l = int(len(name)/2)
    for i in name[0:l]:
        list_name.append(i)
    for i in name[l:len(name)]:
        list_name1.append(i)
        global listToStr
        global listToStr1
        listToStr = "".join(map(str, list_name))
        listToStr1 = "".join(map(str, list_name1))
    return
for ii in range(2):
    dictionary_part_names = {}
    spplit(name=input("Podaj nazwisko :"))
    dictionary_part_names = {"k1": [listToStr, listToStr1]}
print(dictionary_part_names)
