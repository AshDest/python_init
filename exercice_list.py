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

# QUESTION 3 :

# nombres = range(5)
# nombres_doubles = []
# for i in nombres :
#     nombres_doubles.append(i * 2)
# print(nombres_doubles)
# RESOLUTION AVEC LIST COMPREHENSION
# ==================================
nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]
print(nombres_doubles)

# nombres = range(10)
# nombre_inverses = []
# for i in nombres:
#     if i % 2 == 0:
#         nombre_inverses.append(i)
#     else:
#         nombre_inverses.append(-i)
# print(nombre_inverses)


nombres = range(10)
nombre_inverses = [i if i % 2 == 0 else -i for i in nombres ]
print(nombre_inverses)