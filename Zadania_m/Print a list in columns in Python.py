# Print a list in columns in Python
#  https://bobbyhadz.com/blog/python-print-list-in-columns

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# columns = 3
#
# # a         b         c
# # d         e         f
# # g         h         i
# for first, second, third in zip(my_list[::columns], my_list[1::columns], my_list[2::columns]):
#     print(f'{first: <10}{second: <10}{third}')

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(my_list)
print()
print(my_list[::3])  # 👉️ ['a', 'd', 'g']
print(my_list[1::3])  # 👉️ ['b', 'e', 'h']
print(my_list[2::3])  # 👉️ ['b', 'e', 'h']

