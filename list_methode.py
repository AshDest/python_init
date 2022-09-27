# utilisation des methodes dans une liste

from unittest import result


employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

resultat = employes.index("Max") #pour avoir l'index dans la liste, la position
print(resultat)
resultat = employes.count("Max")
print(resultat) # le nombre de fois qu'une valeur se repete dans la liste

employes.sort() # pour groupper les contenu de la liste soit selon lordre croissant
print(employes)