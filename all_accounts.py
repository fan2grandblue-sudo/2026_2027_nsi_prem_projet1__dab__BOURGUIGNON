import json
import os

FICHIER_ACCOUNTS = "accounts.json"

accounts = {
    "fan2riasgremory": {"PIN": "1994", "Solde": 500},
    "Poisson92": {"PIN": "2026", "Solde": 500},
    "Beerlambert12": {"PIN": "0084", "Solde": 500},
}


def charger_accounts():
  global accounts
  if os.path.exists(FICHIER_ACCOUNTS):
    with open(FICHIER_ACCOUNTS, "r", encoding="utf-8") as fichier:
      accounts.clear()
      accounts.update(json.load(fichier))
  else:
    sauvegarder_accounts(accounts)
  return accounts


def sauvegarder_accounts(accounts):
  with open(FICHIER_ACCOUNTS, "w", encoding="utf-8") as fichier:
    json.dump(accounts, fichier, indent=4, ensure_ascii=False)





