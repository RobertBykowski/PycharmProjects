import pandas as pd
from operator import itemgetter
import operator

# file = open("spec.txt", mode = "r", encoding="windows-1250")
# text = file.read()
# text_after_split = text.split(" ")

# aList = ["123", "Ron", "xyz", "zara", "abc", "123", "123", "123","zara", "zara","123", "123", "123"]
# dic ={}
# for i in aList:
#     dic[i] = aList.count(i)
dic ={"Ronn": 1,
      "xyz" : 1,
      "abc" : 1,
      "zara" : 3,
      "123" : 7,}
# a = sorted(dic.items(), key=lambda kv: kv[1])
# print(a)



df = pd.DataFrame.from_dict(dic, orient='index', columns=["Ilość"])
a = df.sort_values(by = ["Ilość"])
print(a)




