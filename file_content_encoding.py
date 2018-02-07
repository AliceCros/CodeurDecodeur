# -*- coding: utf8 -*-

# String de référence contenant les lettres de l'alphabet
dict_input = "abcdefghijklmnopqrstuvwxyz"


def file_content_mystify(source, dest, gap):
    source = open(source, 'r')
    dest = open(dest, 'a')

    key = int(gap)

    for character in source.read():
        if character in dict_input:
            position = dict_input.find(character)
            new_position = (position + key) % len(dict_input)
            new_char = dict_input[new_position]
        else:
            new_char = character
        dest.write(new_char)
    source.close()
    dest.close()
    return dest


source = input("Nom de ton fichier source : ")
dest = input("Nom du fichier destination : ")
gap = input("Quel intervalle ? ")

print(file_content_mystify(source, dest, gap))