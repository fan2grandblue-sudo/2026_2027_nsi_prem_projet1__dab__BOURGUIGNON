from tools import *
from data import *
from menu import *
from all_accounts import *


def register_or_login (language):
    print("\n")
    sign_in = input (translation[language][1]).lower() #demande à l'utilisateur s'il a déjà un compte, et met la réponse en minuscule pour éviter les erreurs de syntaxe
    if sign_in in agree_words or sign_in == "already have one":
        login (language)
    elif sign_in in quit_words:
        exit()
    else:
        account = input(translation[language][2]) #demande à l'utilisateur de choisir un nom de compte
        register (account, language)


def register(account, language):

    if account in accounts: # vérifie si le nom de compte choisi par l'utilisateur existe déjà dans le dictionnaire accounts
        print(translation[language][3])
        register_or_login (language)
    elif account in quit_words:
        exit()
    elif validate_account (account) == True:
        PIN = input(translation[language][4])
        if validate_code (PIN) == True and is_a_number (PIN) == True:
            accounts[account] = {"PIN": PIN, "Solde": 0} # ajoute le nouveau compte à la liste des comptes avec un solde de 0
            print_anim(translation[language][5])
            register_or_login (language)
        else:
            register (account, language)
    else:
        register_or_login (language)
        return
        



def login(language):
    count_false = 1 # variable qui compte le nombre de tentatives de connexion échouées, pour limiter à 3 tentatives
    while count_false <= max_attempts:
        account = input(translation[language][6])
        PIN = input(translation[language][7])
        if account in accounts and accounts[account]["PIN"] == PIN: # vérifie si le nom de compte et le PIN saisis par l'utilisateur correspondent à un compte existant dans le dictionnaire accounts
            print_anim(translation[language][8])
            main_menu (account, language) #exécute la fonction main_menu
            return
        elif account in quit_words:
            exit()
        else:
            print(translation[language][9])
            want_new_account = input(translation[language][10])
            if want_new_account in agree_words:
                register(account, language)
            elif want_new_account in quit_words:
                exit()
            count_false += 1 # ajoute 1 au compteur de tentatives échouées
    print_anim(translation[language][11])
    register_or_login (language)