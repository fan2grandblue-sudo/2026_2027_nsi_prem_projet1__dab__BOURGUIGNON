from tools import *
from all_accounts import *
from data import *

accounts = charger_accounts()

language = pick_language() 

load_bar(5, 100)
print_anim(translation[language][0]) #welcome
print("\n")
from pin_code import *
active = True
while active:
    register_or_login(language)