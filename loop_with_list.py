# list_a = ([23,34,34,67,18])
# for i in range(len(list_a)):
#     print(list_a[i])

file = open("email_ANSI.txt", mode = "r", encoding='windows-1250')
words = file.readlines()
file.close()
a = repr(words)
for i in range(len(a)):
    print(a[i], end="")
