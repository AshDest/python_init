import os

chemin ="C:/Users/hp PC/Documents/Python"
dossier = os.path.join(chemin, "dossier", "test")
if not os.path.exists(dossier):
    os.makedirs(dossier)
os.makedirs(dossier, exist_ok=True)