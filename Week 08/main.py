# main

import sys
import Levenshtein

def check_spelling(word):
    with open(dictionary_file, mode="r") as file:
        dictionary = file.readlines()
        current_gap = len(word)
        current_word = ""
        word = word.lower()
        for dict_word in dictionary:
            if dict_word[0] == word[0]:
                word_gap = Levenshtein.distance(word, dict_word)
                if word_gap < current_gap:
                    current_gap = word_gap
                    current_word = dict_word
                if word_gap == 1:
                    return word
        return current_word

arguments = sys.argv[1:]
input_file = ""
output_file = ""

for i, arg in enumerate(arguments):
    if arg == "-i":
        input_file = arguments[i+1]
    elif arg == "-o":
        output_file = arguments[i+1]
    elif arg == "-d":
        dictionary_file = arguments[i+1]

print(input_file)
print(output_file)
print(dictionary_file)

with open(input_file, mode="r") as file:
    words = [word for lines in file for word in lines.split()]

    with open(output_file, mode="w") as output:
        for word in words:
            print(check_spelling(word), end=" ")

