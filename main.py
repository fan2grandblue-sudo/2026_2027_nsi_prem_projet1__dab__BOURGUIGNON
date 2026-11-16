from tools import *
from all_accounts import *
accounts = charger_accounts()
load_bar(5, 100)
print_anim("WELCOME TO THE ATM\n")
from pin_code import *
active = True
while active:
    register_or_login()