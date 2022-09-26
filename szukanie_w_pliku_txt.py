# file = open("email_ANSI.txt", mode = "r", encoding='cp1250')
file = open("email_ANSI.txt", mode = "r", encoding='windows-1250')
words = file.readlines()
file.close()
a = repr(words)
b= a.index(".pl")
new_tab = []
new_tab_2 = []
tab_content = []
pos = 0

while True:
    try:
        pos = a.index(".com", pos)
        #print(a[pos - 35 : pos + 4])
        new_tab_2.append((a[pos - 35 : pos + 4]))
    except ValueError:
        break
    new_tab.append(pos)
    pos += 1
convert_tab = repr(new_tab_2)
print(convert_tab)
    











            # b = a.rfind(".pl",c)
            # new_tab.append(b)
            # c = len(a) - b
            # print(a[b - 25:b + 3])
            # next_pos = a.index(".pl",b+1)
            # new_tab.append(next_pos)
            # next_pos = a.index(".pl",next_pos+1)
            # new_tab.append(next_pos)








