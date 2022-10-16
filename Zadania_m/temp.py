text = "ola ola ola ala ala ala ala mama tata"
lst = text.split()
list = []
l = []

for idx1, idx2 in zip(lst, lst[1:]):
    if idx1 < idx2:
        continue
    else:
        print(idx1)



