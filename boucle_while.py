import time

i = 0
while i < 10:
    print("Bonjour")
    i += 1

continuer = "o"
while continuer == "o":
    print("On continue...")
    continuer = input("Voulez-vous continuer? o/n ")

while True:
    print("Sauvegarde en cours...")
    time.sleep(600)