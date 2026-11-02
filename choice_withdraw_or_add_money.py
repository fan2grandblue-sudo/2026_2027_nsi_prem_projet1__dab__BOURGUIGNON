from all_accounts import accounts #importe le dictionnaire contenant les comptes, les PIN et les soldes
from fonction_convertisseur import converter # importe la fonction de conversion pour que l'utilisateur puisse convertir son solde en billets et pièces
from data import acceptable_entries

def is_correct (choice):
    return choice in acceptable_entries

def is_not_correct (choice) :
    return not (is_correct (choice))

def choice_withdraw_or_add_money (account):
    choice = str(input("\nDo you want to withdraw or to add money to your account ?  withdraw / add  "))
    choice_made = 0 # servira uniquement à créer une boucle while tant que l'utilisateur n'aura pas fait un choix correct
    while is_not_correct (choice):
        choice = str(input("\nDo you want to withdraw or to add money to your account ?  withdraw / add  "))
    if choice == "withdraw":
        converter () # lance la fonction de conversion pour que l'utilisateur puisse convertir son solde
    elif choice == "add" :
        add_money (account)

    print("\nThank you for using our services ! \nSee you soon ! \n")

def money_added_correct(money_added):


def add_money(account):
    money_added = input("\nHow much do you want to add to your account ?  ")  # servira à redemander une somme à ajouter tant que l'utilisateur n'aura pas rentré un nombre entier
    
    while money_added_correct (money_added) :  #money_added == 0 or type(money_added) != int:
        money_added = input("\nHow much do you want to add to your account ?  ")
    
    accounts[account]["Solde"] = accounts[account]['Solde'] + money_added
    

    
    
    print(f"\nYou now have {accounts[account]['Solde']} on your account ! ")

choice_withdraw_or_add_money (accounts)