row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Enter position : ")
kolumna = int(position[0])
wers = int(position[1])
map[wers-1][kolumna-1] = "x"
print(f"{row1}\n{row2}\n{row3}\n")