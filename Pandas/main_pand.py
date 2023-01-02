import pandas

data = pandas.read_csv("list_of_names.csv")
# print(data)
# dane = input("Pdaj dane: ")
# print(data[data.Nazwisko == dane])
# s_max = data.Wiek.max()
# s_min = data.Wiek.min()
#
#
# print(data[data.Wiek == s_max])
# print(data[data.Wiek == s_min])

# select columns by name
s = data.filter(items=['Nazwisko', 'Wiek'])
# print(s)

#sortowanie wg kolumny
# df = s.sort_values(by='Nazwisko')
# print(df)

df = s.sort_values(by='Wiek')
df.reset_index(drop=True, inplace=True)
df.index = range(1, len(df) + 1)

print(df)