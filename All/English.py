import re
from collections import Counter
import pandas as pd
file = open("spec.txt", mode ="r", encoding="utf-8")
text = file.read()
text_after_split = text.split(" ")

text1 = re.sub(r'\W+'," ", text)
text_after_split = text1.split(" ")
list_regular =set(text_after_split)
print(len(text_after_split))
print(len(list_regular))
print(sorted(list_regular))






