import pandas as pd

s = pd.Series([20, 21, 12],
              index=['London', 'New York', 'Helsinki'])
print(s)

def subtract_custom_value(x, custom_value):
    return x - custom_value

aa= s.apply(subtract_custom_value, args=(5,))
print(aa)
