# -*- coding: utf8 -*-

# Dictionnaire à parcourir initialement
dict_input = "abcdefghijklmnopqrstuvwxyz"

# Suite d'input permettant de paramétrer l'appel de la fonction
file = input("As-tu un fichier à (dé)mystifier ? (o/n)")

if file in ('o', 'O', 'oui', 'OUI', 'y', 'Y', 'yes', 'YES'):
    source_file = input("Indique le chemin du fichier source : ")
    dest_file = input("Indique le chemin vers le fichier destinataire : ")
else:
    # Demande et récupère la variable à convertir
    message = input("Ton message : ")

# Demande et récupère le décalage à calculer (positif ou négatif)
gap = input("Quel décalage ? ")


# Fonction avec 2 arguments (message)
def mystify(message, gap):
    # Cast de gap (string) en int stocké dans la var key
    key = int(gap)
    # Variable vide destinée à contenir le message codé/décodé
    new_message = ''
    # Itération sur chaque lettre de la variable
    for character in message:
        # On gère d'abord les caractères présents dans dict_input
        if character in dict_input:
            # On cherche l'indexation du caractère dans la chaîne de caractère
            position = dict_input.find(character)
            # On calcule la nouvelle indexation du caractère
            # grâce au décalage en paramètre
            new_position = (position + key) % 26
            # On stocke le caractère correspondant à la nouvelle indexation
            new_char = dict_input[new_position]
            # On ajoute chaque nouveau caractère à la var new_message
            new_message += new_char
        # On gère les caractères spéciaux
        else:
            # On ajoute à la chaîne le caractère sans changement
            new_message += character
    return new_message


print(mystify(message, gap))