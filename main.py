from constants import BONJOUR

user = input("Entrer votre prenom: ")
nbre = 10
message = BONJOUR.format(prenom=user, nombre_videos=nbre)
print(message)