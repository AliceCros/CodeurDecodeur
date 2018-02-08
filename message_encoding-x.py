# -*- coding: utf8 -*-

import subprocess

# String de référence contenant les lettres de l'alphabet
alpha_input = "abcdefghijklmnopqrstuvwxyz"


def mystify(gap, message = '', source_file = '', dest_file = ''):
    # Cast de gap (string) en int stocké dans la var key
    key = int(gap)
    # Variable vide destinée à contenir le message codé/décodé
    new_message = ''

    # Si la fonction a été appelée avec un fichier source et destination
    if message == '':
        # On ouvre et on stocke le contenu dans la var message
        content = open(source_file, 'r')
        message = content.readlines()

    # Itération sur chaque lettre de la variable
    for character in message:

        # On gère d'abord les caractères présents dans dict_input
        if character in alpha_input:
            # On cherche l'indexation du caractère dans la chaîne de caractère
            position = alpha_input.find(character)
            # On calcule la nouvelle indexation du caractère
            # grâce au décalage en paramètre
            new_position = (position + key) % 26
            # On stocke le caractère correspondant à la nouvelle indexation
            new_char = alpha_input[new_position]
            # On ajoute chaque nouveau caractère à la var new_message
            new_message += new_char
        # On gère les caractères spéciaux

        else:
            # On ajoute à la chaîne le caractère sans changement
            new_message += character

    # CECI CODE LE NOM DU FICHIER DESTINATION (CA NE COLLE PAS LE NEW_MESSAGE A L'INTERIEUR
    # Si la fonction a été appelé avec un fichier source et destination
    if source_file != '' and dest_file != '':
        # On ouvre le fichier destination et on y ajoute le contenu de new_message
        destination = open(dest_file, 'x')
        destination.write(new_message)
        content.close()
        destination.close()
    return new_message


# Tant que la boucle retourne Vrai...
while True:

    # Confirmation demandée à l'utilisateur
    conf = input("Veux-tu encoder/décoder un message ? (o/n) ")

    # Si le user répond oui...
    if conf in ('o', 'O', 'oui', 'OUI', 'y', 'Y', 'yes', 'YES'):
        # Demande et récupère la variable à convertir
        message = input("Ton message : ")
        # Demande et récupère le décalage à calculer (positif ou négatif)
        gap = input("Quel décalage ? ")
        print(mystify(gap, message))
        # On sort de la boucle
        False

    # Si le user répond non...
    elif conf in ('n', 'N', 'non', 'NON', 'no', 'NO'):
        print()
        print(">> Retour au menu")
        # Redirection sur le Mac de la Coding Factory
        """subprocess.call(["/usr/local/bin/python3.6",
                         "/Users/alice/PycharmProjects/CodeurDecodeur_v1.1/script_menu.py"])"""
        # Redirection sur PC perso
        subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                        "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v1.2/script_menu-x.py"])

    # Si le user répond à côté
    else:
        print("Je ne vous ai pas compris")
        # On refait un tour de boucle si True
        True
