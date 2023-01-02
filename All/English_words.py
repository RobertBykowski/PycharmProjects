import re
from collections import Counter
import pandas as pd
file = open("spec.txt", mode ="r", encoding="utf-8")
text = file.read()
text_after_split = text.split(" ")

text1 = re.sub(r'\W+'," ", text)
text_after_split = text1.split(" ")
list_regular =[]
list_double = []
for i in text_after_split:
    if i in list_regular:
        if i in list_double:
            continue
        else:
            list_double.append(i)
    else:
        list_regular.append(i)
print(len(list_regular))

ind_ex = (len(list_regular))//6
for i in range(ind_ex):
    print(f"{i} {list_regular[i::70]}")



# slownik = Counter(text_after_split)
#
# slownik_sort = sorted(slownik.items(), key=lambda x: x[1], reverse=True)
# df_b = pd.DataFrame(slownik_sort)
# print(df_b)
# print(list_double)
