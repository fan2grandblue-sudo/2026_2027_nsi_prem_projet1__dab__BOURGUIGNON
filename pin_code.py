from menu import menu

accounts = {"fan2riasgremory" : {"PIN" :"995890", "Solde" : 45854},
            "Poisson92" : {"PIN" : "Freedom2026", "Solde" : 85686},
            "Beerlamb12" : {"PIN" : "rrrrrrttttt84", "Solde" : 34}}



def register_or_login ():
    sign_in = input ("\nAlready have an account ? : ").lower()
    if sign_in == "yes" or sign_in == "of course" or sign_in == "already have one" or sign_in == "for sure" or sign_in == "yep":
        login ()
    else:
        register ()


def register():
    account = input("Choose an account name : ")

    if account in accounts:
        print("Account already exists")
        register_or_login ()
    else:
        PIN = input("Choose a PIN : ")
        accounts[account] = {"PIN": PIN, "Solde": 0}
        print("\nAccount created")
        register_or_login ()



def login():
    count_false = 1
    while count_false <= 3 :
        account = input("\nName account : ")
        PIN = input("PIN : ")
        if account in accounts and accounts[account]["PIN"] == PIN:
            print("\nLogin successful")
            menu (account)
            return
        else:
            print("Wrong account or PIN")
            count_false += 1
    print ("Error n1. Please restart")
    register_or_login ()
    
    
    

register_or_login ()