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

* UPDATE 9 NOV. 2026
- lien flowchart architecture : https://miro.com/app/live-embed/uXjVEQPNW_A=/?embedMode=view_only_without_ui&moveToViewport=-1071%2C-462%2C1884%2C934&embedId=42337271438

* UPDATE 10 NOV. 2026
- lien flowchart architecture : https://miro.com/app/live-embed/uXjVEQPNW_A=/?embedMode=view_only_without_ui&moveToViewport=-994%2C-504%2C2147%2C1064&embedId=309815913058

* UPDATE 16 NOV. 2026
- amélioration de l'affichage de la load bar
- création d'un fichier all_accounts qui contient également deux fonctions qui permettent d'enregistrer des comptes (nom, PIN, solde) et sont sauvegardés, même lorsque l'on sort de l'application  ==>  cela modifie donc le fichier json
- fonction_convertisseur : on a fait en sorte que le programme affiche le montant prélever correct (par exemple, il ne doit pas afficher le premier montant prélever si celui-ci est trop grand alors que le user a finalement prélever un montant réglementaire, et donc bien moindre)
- add_money : on a réussi a faire en sorte que si le user ne met pas un montant qui est un nombre, le programme redemande correctement et prend la nouvelle valeur que le user a entré
- début de la création dans data du dictionnaire contenant tous les textes de l'ATM dans différentes langues.

Lien canva : https://canva.link/fz57j3g27sw517e
