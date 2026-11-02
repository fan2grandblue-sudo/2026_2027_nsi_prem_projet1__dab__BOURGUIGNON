# 2026_2027_nsi_prem_projet1__dab
BOURGUIGNON Erwann
BASSIRI Ashkan
SAVKIN Matvey

* UPDATE 5 OCT. 2026
- creation depot
- creations des fichier .gitignore, readme, fonction_convertisseur, pin_code, main

* UPDATE 9 OCT. 2026
Main : fichier a executer
Fonction_convertisseur :
- convertisseur(a) : prend le montant a en entree, et retourne ce montant decompose en nombre de billets optimal
Pin_code :
- show_me_the_money(account) : prend le nom d'un compte (string) en entree, et affiche la solde si demande
- register_or_log_in() : demande si compte existe deja : si oui, renvoie sur login() ; si non, renvoie sur register()
- login() : 3 tentatives pour entrer mot de passe, et si c'est le bon, renvoie sur show_me_the_money(a)
- register() : permet de choisir nom de compte et mot de passe, qu'il ajoute dans la liste des comptes (sauf si compte existe deja), puis renvoie a register_or_log_in()

* UPDATE 2 NOV. 2026
- création d'un fichier all_accounts.py : dictionniaire accounts stockés dedans afin d'eviter les appellations en chaîne
- création d'un fichier tools.py : outils de vérification du bon format des codes et des identifiants
- création d'un fichier data.py : stockage des variables souvent appelées

