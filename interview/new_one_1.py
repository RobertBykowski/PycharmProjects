
import pandas as pd
import numpy as np

file = open("spec.txt", mode = "r", encoding="windows-1250")
text = file.read()
text_after_split = text.split(" ")
dic ={}
for word in text_after_split:
    dic[word] = text_after_split.count(word)

df = pd.DataFrame.from_dict(dic, orient='index', columns=["Ilość"])
a = df.sort_values(by = ["Ilość"], ascending=False)

print("Ilość słów w tekscie:", len(text_after_split))
print(a[0:20])




