# numbers = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1]
# import itertools
# for (key,group) in itertools.groupby(numbers):
#     print (key,list(group))

# l = [0, 0, 0, 1, 1, 2, 0, 0]
# s = itertools.groupby(l)
# print(s)

def nsquare(x, y):
  return (x * x + 2 * x * y + y * y)


print("The square of the sum of 2 and 3 is : ", nsquare(2, 3))