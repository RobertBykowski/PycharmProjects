import numpy as np

import pandas as pd
data2 = ["Test", "test2", "test3"]
data3 = ["Ola", "Ania","Magda"]
# ass = pd.DataFrame(data2, index=["first", "second"])
df1 = pd.DataFrame([data3, data2], columns=["A", "A", "B"])
print(df1)