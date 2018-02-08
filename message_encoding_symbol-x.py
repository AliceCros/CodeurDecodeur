# -*- coding: utf8 -*-

import argparse

parser = argparse.ArgumentParser(description="Crypt your message")
parser.add_argument('-m',
                    "--message",
                    metavar="",
                    required=True,
                    help="Message to be crypted")
parser.add_argument("-g",
                    "--gap",
                    type=int,
                    metavar="",
                    required=True,
                    help="Gap between initial and final character")
args = parser.parse_args()

# String de référence contenant les lettres de l'alphabet
alph_input = "abcdefghijklmnopqrstuvwxyz"
# aleat_input = "[&@#'°%ù/:.>èé'(8743567564"
symb_input = "αβγδεζηθικλμνξοπρςστυφχψω-"


def mystify(gap, message=''):
    # Cast de gap (string) en int stocké dans la var key
    key = int(gap)
    # Variable vide destinée à contenir le message codé/décodé
    new_message = ''

    # Itération sur chaque lettre de la variable
    for character in message:

        # On gère d'abord les caractères présents dans dict_input
        if character in alph_input:
            # On cherche l'indexation du caractère dans la chaîne de caractère
            position = alph_input.find(character)
            # On calcule la nouvelle indexation du caractère
            # grâce au décalage en paramètre
            new_position = (position + key) % 26
            # On stocke le caractère correspondant à la nouvelle indexation
            new_char = symb_input[new_position]
            # On ajoute chaque nouveau caractère à la var new_message
            new_message += new_char
        # On gère les caractères spéciaux

        else:
            # On ajoute à la chaîne le caractère sans changement
            new_message += character

    return new_message


if __name__ == "__main__":
    result = mystify(args.gap, args.message)
    print(result)
