# -*- coding: utf8 -*-

import subprocess # Importation nous servant à ouvrir le script voulu

# On affiche un menu
print()
print("ON CODE ET ON DECODE !")
print("----------------------")
print()
print("QUE VEUX-TU (DE)MYSTIFIER ?")
print()
print("1. UN MESSSAGE (tape 1)")
print("2. UN NOM DE FICHIER (tape 2)")
print("3. LE CONTENU D'UN FICHIER (tape 3)")

# On gère les potentielles exceptions
while True:
    # Le premier try/catch vérifie que le user entre un int
    try:
        choice = int(input("C'EST A TOI : "))
        if choice > 3:
            # Le second try/catch vérifie que le user entre un chiffre entre 1 et 3
            while True:
                try:
                    print()
                    print("Entre 1 et 3, on t'a dit !")
                    choice = int(input("C'EST A TOI : "))
                    break
                except ValueError:
                    print()
                    print("Neiiiin")
        break
    except ValueError:
        print()
        print("Mais qu'est-ce que tu nous raconte là ?")
        print("Allez recommence !")
        print("Et entre un chiffre entre 1 et 3 cette fois !")

if choice == 1:
    subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                     "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v.1.1/message_encoding.py"])
elif choice == 2:
    subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                     "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v.1.1/file_name_encoding.py"])
elif choice == 3:
    subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                     "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v.1.1/file_content_encoding.py"])