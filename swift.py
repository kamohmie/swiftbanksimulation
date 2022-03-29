from os.path import exists as file_exists
try:
    with open(r"bicnamedb.db", 'r') as fp:
        for count, line in enumerate(fp):
            pass
except:
    count = 0

def addbic():
    bicname = input("Quel est le nom de la banque ?")
    bicvalue = input("Quel est le BIC de cette banque ?")
    if file_exists('bic.txt') == False and file_exists('bicname.txt') == False:
        bicnamedb = open("bicname.txt", "w")
        bicvaluedb = open("bic.txt", "w")
        bicnamedb.write(bicname)
        bicvaluedb.write(bicvalue)
        bicnamedb.close()
        bicvaluedb.close()
        print("La banque a bien été ajouté.")
        menuswift()
    else:
        bicnamedb = open("bicname.txt", "a")
        bicvaluedb = open("bic.txt", "a")
        bicnamedb.write(f"\n{bicname}")
        bicvaluedb.write(f"\n{bicvalue}")
        bicnamedb.close()
        bicvaluedb.close()
        print("La banque a bien été ajouté.")
        menuswift()

def send():
    bicmain = input("A quelle banque envoyer de l'argent (BIC):")
    with open("bic.txt", "r") as file:
        file.seek(0)
        global biccount
        biccount = 0
        for line in file.readlines():
            biccount = biccount + 1
            if line.strip("\n") == bicmain:
                bicnamedb = open("bicname.txt", "r")
                bicmainname = bicnamedb.readlines()
                bicnamedb.close()
                global bicdestinataire
                bicdestinataire = bicmainname[biccount-1]
                bicsend = input(f"La banque {bicdestinataire}, doit faire une transaction à (BIC):")
                with open("bic.txt", "r") as file2:
                    global biccount2
                    biccount2 = 0
                    for line2 in file2.readlines():
                        biccount2 = biccount2 + 1
                        if line2.strip("\n") == bicsend:
                            global prix
                            prix = input("Quelle est la valeure de la transaction ($) ?:")
                            bicnamedb = open("bicname.txt", "r")
                            bicsendname = bicnamedb.readlines()
                            bicnamedb.close()
                            global bicdestination
                            bicdestination = bicsendname[biccount2-1]
                            if file_exists('bce.txt') == False:
                                bicvaluedb = open("bce.txt", "w")
                                bicvaluedb.write(f"TRANSACTION : Banque {bicdestinataire} -> {bicdestination} Valeure : {prix}$.\n---")
                                bicvaluedb.close()
                                print(f"Le virement de la banque {bicdestinataire} à la banque {bicdestination} d'un valeure de {prix}$ a bien été fait.")
                                menuswift()
                            else:
                                bicvaluedb = open("bce.txt", "a")
                                bicvaluedb.write(f"\nTRANSACTION : Banque {bicdestinataire} -> {bicdestination} Valeure : {prix}$.\n---")
                                bicvaluedb.close()
                                print(f"Le virement de la banque {bicdestinataire} à la banque {bicdestination} d'un valeure de {prix}$ a bien été fait.")
                                menuswift()
                    else:
                        print("Désolé mais ce BIC n'est relié à aucunes banques.")
        else:
            print("Désolé mais ce BIC n'est relié à aucunes banques.")
            menuswift()
        

def menuswift():
    m1 = input(f"""Bienvenue dans swift !\n
        Swift comporte {count + 1} banque(s).
    [1] Ajouter une banque à swift
    [2] Faire un virement
    [3] Supprimer une banque de swift\nChoix:""")
    if m1 == "1":
        addbic()
    elif m1 == "2":
        send()
    else:
        print("Le choix est invalide.")
        menuswift()
menuswift()
