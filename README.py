# The Ultimate Birds Word Guessing Game!
import random

def choose_word():
    words = ["chicken", "crow", "eagle", "hawk", "parrot", "peacock",
             "penguin", "ostrich", "seagull", "sparrow", "vulture"]
    
    return random.choice(words)