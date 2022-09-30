# liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# nombres_positifs = []
# for i in liste:
#     if i > 0 :
#         nombres_positifs.append(i)

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = [i for i in liste if i > 0] # Liste Comprehension
print(nombres_positifs)