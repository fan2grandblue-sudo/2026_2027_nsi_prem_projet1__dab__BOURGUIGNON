agree_words = ["yes", "of course", "for sure", "yep", "Y", "yurp", "yup", "oui", "oe", "ouaip", "affirmatif", "ui", "ouais"]
quit_words = ["quit", "stop", "terminate", "end", "exit", "fin", "terminer", "quitter"]
max_attempts = 3
acceptable_entries = ["withdraw", "add"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

def pick_language():
     choosing_lang = True
     while choosing_lang:
        language = input("Select language : fr/en/jp/ar/fi/br/gz")
        if language not in translation.keys():
             print_anim("Language invalid.")
        else:
             choosing_lang = False

translation = {
    "fr" : ["BIENVENUE AU DAB",
            "Compte déjà existant ? :",
            "Choisir un nom d'utilisateur",
            "",
            "",
            "",
            ""],
    "en" : ["WELCOME TO THE ATM",
            "Already have an account ? : ",
            "Choose an account name : ",
            "",
            "",
            "",
            ""],
    "ar" : ["ܒܫܝܢܐ ܠܟܘܢ ܠܡܟܢܫܬܐ ܕܟܣܦܐ",
            "ܐܝܬ ܠܟ ܚܘܫܒܢܐ ܡܢ ܩܕܡ ؟ :",
            "ܓܒܝ ܫܡܐ ܕܚܘܫܒܢܐ :",
            "",
            "",
            "",
            ""],
    "jp" : ["ATMへようこそ",
            "すでにアカウントを持っていますか？",
            "アカウント名を選んでね：",
            "",
            "",
            "",
            ""],
    "fi" : ["TERVETULOA PANKKIAUTOMAATILLE",
            "Onko sinulla jo tili ? :",
            "Valitse tilin nimi :",
            "",
            "",
            "",
            ""],
    "br" : ["⠠⠠⠺⠑⠇⠉⠕⠍⠑ ⠠⠠⠞⠕ ⠠⠠⠞⠓⠑ ⠠⠠⠁⠞⠍",
            "⠠⠁⠇⠗⠑⠁⠙⠽ ⠓⠁⠧⠑ ⠁⠝ ⠁⠉⠉⠕⠥⠝⠞ ⠦ ⠒",
            "⠠⠉⠓⠕⠕⠎⠑ ⠁⠝ ⠁⠉⠉⠕⠥⠝⠞ ⠝⠁⠍⠑ ⠒",
            "",
            "",
            "",
            ""],
    "gz" : ["LIL BRO SPAWNED INTO THE ATM",
            "Is broski an OG ? : ",
            "Pick a username you finna be stuck with : ",
            "",
            "",
            "",
            ""],
}