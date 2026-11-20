from pin_code import *
from tools import *
from data import *
from fonction_convertisseur import *
from add_money import *



def main_menu (account, language):
    longline ()
    print_anim (translation[language][12])
    print_anim (translation[language][13])
    print_anim (translation[language][14])
    print_anim (translation[language][15])
    print_anim (translation[language][16])
    answer = input (translation[language][17])
    if answer == "1" :
        show_me_the_money (account, language)
    elif answer == "2" :
        add_money (account, language)
    elif answer == "3" :
        converter (account, language)
    elif answer == "4" :
        language = pick_language() 
    elif answer == "5":
        sauvegarder_accounts(accounts)
        print_anim (translation[language][18])
        print_anim (translation[language][19])
        load_dots(1, 3)
        exit ()
    else:
        print (translation[language][20])
    sauvegarder_accounts(accounts)
    main_menu (account, language)

    



def show_me_the_money (account, language):

    print_anim (("You have ",accounts[account]["Solde"], " €\n")) #print le solde du compte de l'utilisateur

