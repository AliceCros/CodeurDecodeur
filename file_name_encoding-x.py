# -*- coding: utf8 -*-
""" Ce programme a pour objectif de traduire (encoder/décoder) des noms de fichiers"""

# Importation d'os pour le renommage des fichiers
import os
import subprocess

# String de référence contenant les lettres de l'alphabet
alpha_input = "abcdefghijklmnopqrstuvwxyz"

# Pour sauvegarder les noms de fichiers encodés et leur gap
encoded_files = {}


def file_name_mystify(file, gap=''):
    """Fonction file_name_mystify qui prend en argument le nom du fichier
    le décalage de caractère souhaité"""
    key = 0
    # Dans le cas d'un décodage
    # on veut retrouver le gap appliqué lors de l'encodage
    if gap == '':
        gap = encoded_files.get(file)
        key -= int(gap)
    else:
        key = int(gap)

    new_file = ''

    # On passe en revue chaque caractère du nom du fichier
    for character in file:
        if character in alpha_input:
            # Si on retrouve le caractère dans l'alphabet
            # on prend la position et on lui ajoute le gap pour encoder / décoder
            position = alpha_input.find(character)
            new_position = (position + key) % len(alpha_input)
            new_file += alpha_input[new_position]
        else:
            # Si on a affaire à un caractère spécial
            # on le conserve tel quel
            new_file += character
    file = os.replace(file, new_file) # Fonction pour modifier le nom du fichier

    # Si on encode un nom de fichier
    # on conserve son nom encodé et son gap dans un tuple
    if key > 0:
        encoded_files[new_file] = key
    else:
        pass
    return new_file


while True:
    action = input("Souhaite-tu encoder ou décoder un nom de fichier ? (e/d) ")
    if action in ('e', 'E'):
        file_name = input("Nom de ton fichier : ")
        gap_file = input("Quel intervalle ? ")
        print(file_name_mystify(file_name, gap_file))
    elif action not in ('e', 'E', 'd', 'D'):
        print("Ce n'est pas ma question O_o")
        True
    else:
        file_name = input("Nom de ton fichier : ")
        print(file_name_mystify(file_name))
        False
    ok = input("'C' pour continuer, 'S' pour sortir : ")
    if ok == 'S':
        # Redirection sur le Mac de la Coding
        """subprocess.call(["/usr/local/bin/python3.6",
                         "/Users/alice/PycharmProjects/CodeurDecodeur_v1.1/script_menu.py"])"""
        # Redirection sur PC perso
        subprocess.call(["C:/Users/Alice/AppData/Local/Programs/Python/Python36-32/python.exe",
                        "C:/Users/Alice/PycharmProjects/CodeurDecodeur_v1.2/script_menu-x.py"])
    else:
        True
