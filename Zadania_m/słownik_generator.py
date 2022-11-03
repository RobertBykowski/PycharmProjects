listaA = ["Id","Name", "F_name", "City"]
listaB = [123, "Ron", "Poter", "New_York"]
res = {}
# for key in listaA:
#     for value in listaB:
#         res[ key ] = value
#         listaB.remove(value)
#         break
# res = {listaA[i]: listaB[i] for i in range(len(listaA))}
res = dict(zip(listaA, listaB))
# Printing resultant dictionary
print(res)