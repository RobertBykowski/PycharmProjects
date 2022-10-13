name_1 = "Robert Bykowski" #input("Enter name_1: ")
name_2 = " Tom Nowakowski" #input("Enter name_2: ")
sum_names = name_1+name_2
#-------------------------------
list = []
for i in range(len(sum_names)):
    while sum_names[i] == " ":
        list.append(i)
        i += 1
    else:
        continue

print(list)
print(sum_names[0:list[0]])
print(sum_names[list[0]+1:list[1]])
print(sum_names[list[1]+1:list[2]])
print(sum_names[list[2]+1:list[2]+len(sum_names)])
print("index 1/2",list[0]/2)
print("index 1/2",list[1]/2)
print("index 1/2",list[2]/2)
print("index 1/2",(list[2]+1)/2)
