import os
import json
import random

with open(os.path.join("cowsandbulls", "data", "words_dictionary.json"), 'r') as jsonfile:
    data = json.load(jsonfile)
dictionary = list(data.keys())

with open(os.path.join("cowsandbulls", "data", "common.json"), 'r') as jsonfile:
    data = json.load(jsonfile)
word_list = data["commonWords"]

def get_random_word(length):
    word = ""
    while len(word) != length or does_contain_repeated_words(word):
        word = random.choice(word_list)
    return word

def is_not_valid_word(word):
    return not word in dictionary

def is_different_length(my_word, guessed_word):
    return len(my_word) != len(guessed_word)

def does_contain_repeated_words(guessed_word):
    return len(set(guessed_word)) != len(guessed_word)

def is_win(my_word, guessed_word):
    return my_word == guessed_word

def calculate_bulls_and_cows(my_word, guessed_word):
    total_count = len(set(my_word) & set(guessed_word))
    bulls = 0
    for i,j in zip(my_word, guessed_word):
        if (i==j):
            bulls +=1
    return {"Word": guessed_word, "Bulls": bulls, "Cows": total_count - bulls}