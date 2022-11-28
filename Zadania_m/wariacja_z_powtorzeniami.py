#Wariacja z powtórzeniami

import itertools
import pandas as pd
# for v in itertools.combinations_with_replacement(["F","T"], 3):
#     print(v)
a = []
for v in itertools.product(["F","T"], repeat=3):
    a.append(v)
print(a[0])
for i in a[0]:
    print(i)


# df_a = pd.DataFrame(a)
#
# df_a.insert(0, "Kolumna", ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"], True)
# df_a.columns = "Kolumna", 'A', 'B',"C",
# print(df_a)

