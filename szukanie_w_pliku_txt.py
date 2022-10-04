import re
# file = open("email_ANSI.txt", mode = "r", encoding='cp1250')
file = open("email_ANSI.txt", mode = "r", encoding='windows-1250')
words = file.readlines()
file.close()
a = repr(words)
b= a.index(".com")
new_tab = []
new_tab_2 = []
tab_content = []
pos = 0

while True:
    try:
        pos = a.index((".com"), pos)
        #print(a[pos - 35 : pos + 4])
        new_tab_2.append((a[pos - 30 : pos + 4]))

    except ValueError:
        break
    new_tab.append(pos)
    pos += 1

convert_tab = repr(new_tab_2)
tab_end = []
for element in convert_tab:
    convert_tab_1 = re.findall(r"\w+@\w+\.com", convert_tab, re.MULTILINE)#.group()
    tab_end= set(convert_tab_1)
print(f"Data of newsletters: \n{tab_end}\n")
f = open("wynik2.txt",mode='w')
tab_end_end = map(lambda x: x+'\n',tab_end)
f.writelines(tab_end_end)
f.close()













    



















