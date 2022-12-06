# def my_function(*kids):
#   for kid in kids:
#     print("The youngest child is " + kid)
#
# my_function("Emil", "Tobias", "Linus")
products = ["cherry", "strawberry", "banana"]
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is {p-c}!')