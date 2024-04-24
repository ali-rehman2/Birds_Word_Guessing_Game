# The Ultimate Birds Word Guessing Game!
import random

def choose_word():
    words = ["chicken", "crow", "eagle", "hawk", "parrot", "peacock",
             "penguin", "ostrich", "seagull", "sparrow", "vulture"]
    
    return random.choice(words)

def word_ranking(word, guessed_letters):
    present = ""
    for letter in word:
        if letter in guessed_letters:
            present += letter 
        else:
            present += "_"

    return present