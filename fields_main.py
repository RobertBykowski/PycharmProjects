znak = ["X", ".", "*"]
for index in range(len(znak)):
        fields_file = open("fields.txt", "a")
        fields_file.readable()
        znak_bis = map(lambda x: x+"\n", znak * 3)
        fields_file.writelines(znak_bis)
        fields_file.close()
print(znak_bis)


