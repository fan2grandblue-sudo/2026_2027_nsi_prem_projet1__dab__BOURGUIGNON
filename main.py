from tools import *
from all_accounts import *
from data import *
accounts = charger_accounts()
global language
choosing_lang = True
while choosing_lang:
    language = input("Select language : fr/en/jp/ar/fi/br/gz")
    if language not in translation.keys():
        print_anim("Language invalid.")
    else:
        choosing_lang = False
load_bar(5, 100)
print_anim(translation[language][0]) #welcome
print("\n")
from pin_code import *
active = True
while active:
    register_or_login()