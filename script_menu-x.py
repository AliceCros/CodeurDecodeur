# -*- coding: utf8 -*-

# Importation nous servant à ouvrir le script voulu
import subprocess

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
print("X. FERMER LE PROGRAMME (tape X)")

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
        if choice == 'X':
            exit()
            False
        break
    except ValueError:
        print()
        print("Mais qu'est-ce que tu nous raconte là ?")
        print("Allez recommence !")
        print("Et entre un chiffre entre 1 et 3 cette fois !")

# Redirection sur le Mac de la Coding Factory
"""if choice == 1:
    subprocess.call(["/usr/local/bin/python3.6",
                     "/Users/alice/PycharmProjects/CodeurDecodeur_v1.2/message_encoding.py"])
elif choice == 2:
    subprocess.call(["/usr/local/bin/python3.6",
                     "/Users/alice/PycharmProjects/CodeurDecodeur_v1.2/file_name_encoding.py"])
elif choice == 3:
    subprocess.call(["/usr/local/bin/python3.6",
                     "/Users/alice/PycharmProjects/CodeurDecodeur_v1.2/file_content_encoding.py"])
elif choice == 'X':
    exit()"""

# Redirection sur PC perso
if choice == 1:
    subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                     "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v1.2/message_encoding-x.py"])
elif choice == 2:
    subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                     "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v1.2/file_name_encoding-x.py"])
elif choice == 3:
    subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                     "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v1.2/file_content_encoding-x.py"])
