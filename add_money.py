from fonction_convertisseur import converter # importe la fonction de conversion pour que l'utilisateur puisse convertir son solde en billets et pièces
from data import *
from tools import *
from all_accounts import *


def money_added_correct(money_added):
    for character in money_added:
        if character not in numbers : # vérifie si chaque caractère du montant est un entier naturel
            return False
    return True


def add_money(account, language):
    #money_added = str(input("\nHow much do you want to add to your account ?  "))  # servira à redemander une somme à ajouter tant que l'utilisateur n'aura pas rentré un nombre entier
    boolean = False
    while boolean == False : # exécute la fonction qui vérifie si l'entrée est bien un entier naturel
        money_added = str(input(translation[language][21]))
        boolean = money_added_correct (money_added)
    
    accounts[account]["Solde"] = int(accounts[account]["Solde"]) + int(money_added)
    

    
    
    print_anim (f"\n{translation[language][38]} {accounts[account]['Solde']} {translation[language][39]}")