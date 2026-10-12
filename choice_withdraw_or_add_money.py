from all_accounts import accounts #importe le dictionnaire contenant les comptes, les PIN et les soldes

def choice_withdraw_or_add_money (account):
    choice = str(input("\nDo you want to withdraw or to add money to your account ?  withdraw / add  "))
    a = 0
    while a == 0:
        if choice == "withdraw":
            from fonction_convertisseur import converter #importe la fonction de conversion pour que l'utilisateur puisse convertir son solde en billets et pièces
            converter () #lance la fonction de conversion pour que l'utilisateur puisse convertir son solde
            return "\n"
            a = 1 # arrete la boucle while qui demande si on veut ajouter ou prélever de l'argent
        elif choice == "add" :
            add_money (account)
            a = 1
        else :
            withdraw = str(input("\nDo you want to withdraw or to add money to your account ?  withdraw / add  "))
    

def add_money(account):
    money_added = int(input("\nHow much do you want to add to your account ?"))
    accounts[account]["Solde"] += money_added
    return f"\nYou now have {accounts[account]["Solde"]} on your account !"

choice_withdraw_or_add_money (accounts)