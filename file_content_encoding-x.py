#  -*- coding: utf-8 -*-

# String de référence contenant les lettres de l'alphabet
alpha_input = "abcdefghijklmnopqrstuvwxyz"


def file_content_mystify(source, dest, gap):
    source = open(source, 'r')
    dest = open(dest, 'a')

    key = int(gap)

    for character in source.read():
        if character in alpha_input:
            position = alpha_input.find(character)
            new_position = (position + key) % len(alpha_input)
            new_char = alpha_input[new_position]
        else:
            new_char = character
        dest.write(new_char)
    source.close()
    dest.close()
    return dest


source_file = input("Nom de ton fichier source : ")
dest_file = input("Nom du fichier destination : ")
gap_file = input("Quel intervalle ? ")

res = file_content_mystify(source_file, dest_file, gap_file)
print(res)
