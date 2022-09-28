# utilisation des methodes dans une liste

employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

resultat = employes.index("Max") #pour avoir l'index dans la liste, la position
print(resultat)
resultat = employes.count("Max")
print(resultat) # le nombre de fois qu'une valeur se repete dans la liste

employes.sort() # pour groupper les contenu de la liste soit selon lordre croissant
print(employes)

employes.reverse() # Pour inverser l'ordre dans une liste
print(employes)

employes.pop(-1) # pour enlever un element de la liste a partir de son index
print(employes)

employes.clear() # pour supprimer tous les elements des la liste
