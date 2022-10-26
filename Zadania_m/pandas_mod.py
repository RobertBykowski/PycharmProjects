import pandas as pd

a = [['Ania',24, 3400],['Michał',9, 5400],['Darek',40, 6000],['Ewa',43,7890]]
df_a = pd.DataFrame(a)
df_a.columns = 'Imię', 'Wiek', 'Wypłata'
a = df_a.sort_values(by = ["Wypłata"], ascending=False)
# print(df_a[0:2])
print(a)


