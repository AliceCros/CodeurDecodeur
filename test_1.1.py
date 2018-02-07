# -*- coding: utf8 -*-

# Dictionnaire à parcourir initialement
dict_input = "abcdefghijklmnopqrstuvwxyz"


def mystify(gap, message = '', source_file = '', dest_file = ''):
    # Cast de gap (string) en int stocké dans la var key
    key = int(gap)
    # Variable vide destinée à contenir le message codé/décodé
    new_message = ''

    # Si la fonction a été appelée avec un fichier source et destination
    if source_file != '' and dest_file != '':
        # On ouvre et on stocke le contenu dans la var message
        content = open(source_file)
        message = content.read()

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

    # CECI CODE LE NOM DU FICHIER DESTINATION (CA NE COLLE PAS LE NEW_MESSAGE A L'INTERIEUR
    # Si la fonction a été appelé avec un fichier source et destination
    if source_file != '' and dest_file != '':
        # On ouvre le fichier destination et on y ajoute le contenu de new_message
        destination = open(dest_file)
        destination.write(new_message)
    return new_message


# Question à l'utilisateur sur ce qu'il veut faire
file = input("As-tu un fichier à (dé)mystifier ? (o/n) ")

# Tant que la boucle retourne Vrai...
while True:

    # Si le user répond oui...
    if file in ('o', 'O', 'oui', 'OUI', 'y', 'Y', 'yes', 'YES'):
        # Nous pouvons lui demander les fichiers source et dest
        source_file = input("Indique le chemin du fichier source : ")
        dest_file = input("Indique le chemin vers le fichier destinataire : ")
        # Demande et récupère le décalage à calculer (positif ou négatif)
        gap = input("Quel décalage ? ")
        print(mystify(gap, source_file, dest_file))
        False  # On sort de la boucle

    # Si le user répond non...
    elif file in ('n', 'N', 'non', 'NON', 'no', 'NO'):
        # Demande et récupère la variable à convertir
        message = input("Ton message : ")
        # Demande et récupère le décalage à calculer (positif ou négatif)
        gap = input("Quel décalage ? ")
        print(mystify(gap, message))
        False  # On sort de la boucle

    # Si le user répond à côté
    else:
        print("Je ne vous ai pas compris")
        file = input("As-tu un fichier à (dé)mystifier ? (o/n) ")
        True  # On refait un tour de boucle