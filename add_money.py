from fonction_convertisseur import converter # importe la fonction de conversion pour que l'utilisateur puisse convertir son solde en billets et pièces
from data import *
from tools import *
from all_accounts import *


def money_added_correct(money_added):
<<<<<<< HEAD
    for character in money_added:
        if character not in numbers : # vérifie si chaque caractère du montant est un entier naturel
            return False
    return True
=======
    money_added_list = [] # met le montant à ajouter sous forme de liste pour ensuite parcourir chaque caractère du montant et vérifier qu'il sont tous des entiers naturels
    for i in range (len(money_added)):
        money_added_list.append(money_added)
    
    for i in range (len(money_added)):
        if money_added_list[i] not in numbers : # vérifie si chaque caractère du montant est un entier naturel
            money_added_list = [] # réinitialise la liste pour une nouvelle entrée
            return True
    return False
>>>>>>> f90a123e4f6aeaa91db9d3905929bf12a0a8ca9b


def add_money(account):
    #money_added = str(input("\nHow much do you want to add to your account ?  "))  # servira à redemander une somme à ajouter tant que l'utilisateur n'aura pas rentré un nombre entier
    boolean = False
    while boolean == False : # exécute la fonction qui vérifie si l'entrée est bien un entier naturel
        money_added = str(input("\nHow much do you want to add to your account ?  "))
        boolean = money_added_correct (money_added)
    
    accounts[account]["Solde"] = int(accounts[account]["Solde"]) + int(money_added)
    

    
    
    print_anim (f"\nYou now have {accounts[account]['Solde']} on your account ! ")


#add_money (account)