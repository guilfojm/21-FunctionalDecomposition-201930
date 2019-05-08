"""
Hangman.

Authors: Justin Guilfoyle and Lauren Copeland
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random

def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0,len(words))
        item = words[r]


####### Do NOT attempt this assignment before class! #######

