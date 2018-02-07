# -*- coding: utf8 -*-
# Ce programme a pour objectif de traduire (encoder/décoder) les noms de fichiers

import os # Importation d'os pour le renommage des fichiers

# String de référence contenant les lettres de l'alphabet
dict_input = "abcdefghijklmnopqrstuvwxyz"

# Pour sauvegarder les noms de fichiers encodés et leur gap
encoded_files = {}


def file_name_mystify(action, file, gap = ''):

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
        if character in dict_input:
            # Si on retrouve le caractère dans l'alphabet
            # on prend la position et on lui ajoute le gap pour encoder / décoder
            position = dict_input.find(character)
            new_position = (position + key) % len(dict_input)
            new_file += dict_input[new_position]
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
    return file


while True:
    action = input("Souhaite-tu encoder ou décoder un nom de fichier ? (e/d) ")
    file = input("Nom de ton fichier : ")
    if action in ('e', 'E'):
        gap = input("Quel intervalle ? ")
        #if type(gap) != int:
        #    print("Par contre, on va avoir besoin d'un nombre pour t'aider")
        #    gap = input("Quel intervalle veux-tu appliquer ? (en chiffre) ")
        #else:
        #    False
        print(file_name_mystify(action, file, gap))
        False
    elif action not in ('e', 'E', 'd', 'D'):
        print("Ce n'est pas ma question O_o")
        action = input("Souhaite-tu encoder ou décoder un nom de fichier ? (e/d) ")
        True
    else:
        print(file_name_mystify(action, file))
        False