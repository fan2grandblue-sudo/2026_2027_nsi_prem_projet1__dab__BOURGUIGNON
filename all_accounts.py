import json

accounts = {"fan2riasgremory" : {"PIN" :"1994", "Solde" : 500},
            "Poisson92" : {"PIN" : "2026", "Solde" : 500},
            "Beerlambert12" : {"PIN" : "0084", "Solde" : 500}} #dictionnaire contenant les comptes, les PIN et les soldes de chaque user

# Crée ou écrase le fichier 'donnees.json' dans le dossier de votre projet
with open("donnees.json", "w", encoding="utf-8") as fichier:
  json.dump(accounts, fichier, indent=4, ensure_ascii=False)

import json

with open("donnees.json", "r", encoding="utf-8") as fichier:
  accounts = json.load(fichier)


