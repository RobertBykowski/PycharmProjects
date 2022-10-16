
james = [10,20,76,45,34,17,15,10,20]
print(james)
unique_james = []
for each_t in james:
    for each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])