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

def word_guessing_game():
    unrevealed_word = choose_word()
    guessed_letters = []
    attempts = 3

    print("Word Guessing Game")
    print("******************")
    print("Unrevealed Word:", word_ranking(unrevealed_word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter.")
            continue  

