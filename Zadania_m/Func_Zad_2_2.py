# def list_of_numbers(n):
#     list_b = list(range(1,n+1,2))
#     print(list_b)
#     print(len(list_b))
#     for i in list_b:
#         print(i)
#
# list_of_numbers(10)

def list_name():
    list_names_1 = ["Ala", "Ola", "Adam", "Tomasz"]
    list_names_2 = ["Alaxa", "Olax", "Adamx", "Tomaszx"]
    for _ in list_names_1, list_names_2:
      print(_, end="")
list_name()