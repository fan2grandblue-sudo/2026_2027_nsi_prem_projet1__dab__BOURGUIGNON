from all_accounts import accounts #importe le dictionnaire contenant les comptes, les PIN et les soldes
from tools import *
from data import *

def show_me_the_money (account):

    balance = input ("\nShow me the money ? : ").lower() #demande à l'utilisateur s'il veut voir son solde, et met la réponse en minuscule pour éviter les erreurs de syntaxe
    if balance in ["show me the money", "show me my money"] or balance in agree_words:
        print(accounts[account]["Solde"], "€") #print le solde du compte de l'utilisateur
        
    elif balance == "balance unlimited":
        accounts[account]["Solde"] = 9999999999999999  #solde illimité pour le compte de l'utilisateur
        print(accounts[account]["Solde"], "€")
    
    elif balance == "greed never dies":
        import assassin_hub
    
    elif balance in quit_words:
        exit()

    else:
        from fonction_convertisseur import converter #importe la fonction de conversion pour que l'utilisateur puisse convertir son solde en billets et pièces
        converter () #lance la fonction de conversion pour que l'utilisateur puisse convertir son solde



def register_or_login ():
    sign_in = input ("\nAlready have an account ? : ").lower() #demande à l'utilisateur s'il a déjà un compte, et met la réponse en minuscule pour éviter les erreurs de syntaxe
    if sign_in in agree_words or sign_in == "already have one":
        login ()
    elif sign_in in quit_words:
        exit()
    else:
        account = input("Choose an account name : ") #demande à l'utilisateur de choisir un nom de compte
        register (account)


def register(account):

    if account in accounts: # vérifie si le nom de compte choisi par l'utilisateur existe déjà dans le dictionnaire accounts
        print("Account already exists")
        register_or_login ()
    elif account in quit_words:
        exit()
    elif validate_account (account) == True:
        PIN = input("Choose a PIN : ")
        if validate_code (PIN) == True and is_a_number (PIN) == True:
            accounts[account] = {"PIN": PIN, "Solde": 0} # ajoute le nouveau compte à la liste des comptes avec un solde de 0
            print("\nAccount created")
            register_or_login ()
        else:
            register (account)
    else:
        register_or_login ()
        return
        



def login():
    count_false = 1 # variable qui compte le nombre de tentatives de connexion échouées, pour limiter à 3 tentatives
    while count_false <= max_attempts:
        account = input("\nName account : ")
        PIN = input("PIN : ")
        if account in accounts and accounts[account]["PIN"] == PIN: # vérifie si le nom de compte et le PIN saisis par l'utilisateur correspondent à un compte existant dans le dictionnaire accounts
            print("\nLogin successful")
            show_me_the_money(account) #exécute la fonction show_me_the_money pour afficher le solde du compte de l'utilisateur et lui permettre de convertir une partie de son solde en billets et pièces
            return
        elif account in quit_words:
            exit()
        else:
            print("Wrong account or PIN")
            want_new_account = input("Want to create a new account instead? ")
            if want_new_account in agree_words:
                register(account)
            elif want_new_account in quit_words:
                exit()
            count_false += 1 # ajoute 1 au compteur de tentatives échouées
    print ("Error n1. Please restart")
    register_or_login ()

register_or_login()
            
        