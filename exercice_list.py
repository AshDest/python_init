# QUESTION 1 : 
# nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
# nombres_paires = []
# for i in nombres:
#     if i % 2 == 0:
#         nombres_paires.append(i)
        
# print(nombres_paires)

# RESOLUTION AVEC LIST COMPREHENSION
# ==================================
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_paires = [i for i in nombres if i % 2 == 0]
print(nombres_paires)

# QUESTION 2 :

# nombres = range(-10,10)
# nombres_positifs = []
# for i in nombres :
#     if i >= 0 :
#         nombres_paires.append(i)
# print(nombres_paires)
# RESOLUTION AVEC LIST COMPREHENSION
# ==================================
nombres = range(-10,10)
nombres_positifs = [i for i in nombres if i > 0 ]
print(nombres_positifs)