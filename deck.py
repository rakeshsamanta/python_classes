#importing modules
import itertools, random

#make a deck of cards
deck = list(itertools.product(range(1,14),['spade','heart','diamond','club']))

#shuffle the card
random.shuffle(deck)

#draw five cards
print("you got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])