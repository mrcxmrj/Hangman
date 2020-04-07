import random

with open("dictionary.txt", "r") as dictionary:
    words = [line for line in dictionary]
word = random.choice(words)
print(word)