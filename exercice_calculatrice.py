nbre1 = input("Entrer le premier nombre : ")
while not nbre1.isdigit():
    print("Valeur Nombre 1 Invalide!!")
    nbre1 = input("Entrer le premier nombre : ")
nbre2 = input("Entrer le deuxieme nombre : ")
while not nbre2.isdigit():
    print("Valeur Nombre 2 Invalide!!")
    nbre2 = input("Entrer le deuxieme nombre : ")
print(f"Le resultat de l'addition de {nbre1} avec {nbre2} est egal à {int(nbre1) + int(nbre2)}")