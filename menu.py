from pin_code import accounts


def show_me_the_money (account):
    balance = input ("\nShow me the money ? : ").lower()
    if balance in ["yes", "of course", "show me the money", "show me my money", "for sure", "yep"]:
        print(accounts[account]["Solde"], "€")
        
    elif balance == "balance unlimited":
        accounts[account]["Solde"] = 9999999999999999
        print(accounts[account]["Solde"], "€")

    menu (account)



def deposit_money (account):
    how_much = int (input ("\nHow much do you want to deposit ? : "))
    if how_much <= 0:
        print("Please enter a positive amount.")
    elif how_much > 1000:
        print ("To much to realise this operation. Pick a number below 1500€ please.\nOr please book an appointment with one of our on-site assistants")
    else:
        accounts[account]["Solde"] = accounts[account]["Solde"] + how_much
    menu (account)




def menu (account):
    what_to_do_next = input ("\nAccount Balance, Withdraw Money, Deposit Money, Exit ? : ").lower()
    if what_to_do_next == "account balance":
            show_me_the_money(account)

    elif what_to_do_next == "withdraw money":
        import fonction_convertisseur

    elif what_to_do_next == "deposit money":
        deposit_money(account)

    elif what_to_do_next == "exit":
        print("Logged out successfully.")
    else:
        print("Choose one of the operations above.")

menu (accounts)



