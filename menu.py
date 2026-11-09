from pin_code import *
from tools import *
from data import *
from fonction_convertisseur import *
from add_money import *



def main_menu (account):
    longline ()
    print_anim ("\n1 - Show Bank Account")
    print_anim ("\n2 - Add money")
    print_anim ("\n3 - Withdraw money")
    print_anim ("\n4 - Settings")
    print_anim ("\n5 - Logout")
    answer = input ("\nChoose an operation : ")
    if answer == "1" :
        show_me_the_money (account)
    elif answer == "2" :
        add_money (account)
    elif answer == "3" :
        converter (account)
    elif answer == "4" :
        pass
        #settings ()
    elif answer == "5":
        print_anim ("\nThanks for using our ATM") 
        print_anim ("\nSee you soon !\n")
        load_dots(1, 3)
        exit ()
    else:
        print ("Please choose one of the operation above")
        main_menu (account)

    



def show_me_the_money (account):

    print(accounts[account]["Solde"], "€") #print le solde du compte de l'utilisateur
    
    main_menu (account)