from all_accounts import accounts #importe le dictionnaire contenant les comptes, les PIN et les soldes

def choice_withdraw_or_add_money (account):
    choice = str(input("\nDo you want to withdraw or to add money to your account ?  withdraw / add  "))
    choice_made = 0 # servira uniquement à créer une boucle while tant que l'utilisateur n'aura pas fait un choix correct
    while choice_made == 0:
        if choice == "withdraw":
            from fonction_convertisseur import converter # importe la fonction de conversion pour que l'utilisateur puisse convertir son solde en billets et pièces
            converter () # lance la fonction de conversion pour que l'utilisateur puisse convertir son solde
            #print ("\n")
            #choice_made = 1
        elif choice == "add" :
            add_money (account)
            #choice_made = 1
            break
        else :
            choice = str(input("\nDo you want to withdraw or to add money to your account ?  withdraw / add  "))
    print("\nThank you for using our services ! \nSee you soon ! \n")


def add_money(account):
    amount_added = 0 # servira à redemander une somme à ajouter tant que l'utilisateur n'aura pas rentré un nombre entier
    while amount_added == 0:
        money_added = int(input("\nHow much do you want to add to your account ?  "))
        if money_added is int:
            accounts[account]["Solde"] = accounts[account]['Solde'] + money_added
            money_added = 1
        else:
            money_added = int(input("\nHow much do you want to add to your account ?  "))
    
    
    return f"\nYou now have {accounts[account]['Solde']} on your account !"

choice_withdraw_or_add_money (accounts)