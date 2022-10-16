name_1 = "Robert Bykowski" #input("Enter name_1: ")
name_2 = "Tomasz Nowakowski" #input("Enter name_2: ")
name_2 = name_2.lower()
#-------------------------------
def split_names (name):
    space = name.find(" ")
    space_05 = int(space/2)
    l2 = int((len(name) - space)/2)
    # global name_f, f_name
    name_f = (name[0:space_05])
    f_name = (name[space+1:space+l2])
    return name_f, f_name

b = split_names(name_1)
c = split_names(name_2)
print(b)
print(c)
print(f"{b[0]+c[0]} {b[1]+c[1]}")

