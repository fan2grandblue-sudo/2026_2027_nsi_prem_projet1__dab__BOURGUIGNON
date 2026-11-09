from tools import *
from data import *
from menu import *


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
            print_anim("\nAccount created")
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
            print_anim("\nLogin successful\n")
            main_menu (account) #exécute la fonction main_menu
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
    print_anim("Error n1. Please restart")
    register_or_login ()
            
        