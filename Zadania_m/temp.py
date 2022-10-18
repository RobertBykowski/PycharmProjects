# text = "ola ola ola ala ala ala ala mama tata"
# lst = text.split()
# list = []
# l = []
#
# for idx1, idx2 in zip(lst, lst[1:]):
#     if idx1 < idx2:
#         continue
#     else:
#         print(idx1)

# a_list = ['bobby', 'hadz', 'com', "ali"]
#
# result = '--'.join(a_list)
# print(result) # 👉️ bobby   hadz    com

def druk (name1, name2, name3, name4):
    return sorted((name1, name2, name3, name4))

list = ["Ala", "Ola", "Magda",1]

print(druk(*list))