#card

import random
import os
 
#card class definition
class Card:
    def _int_(self,suit,value):
        self.suit=suit
        self.value=value

#The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
# The suit value 
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
# The card value
cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
 
# The deck of cards
deck = []
 
# Loop for every type of suit
for suit in suits:
 
    # Loop for every type of card in a suit
    for card in cards:
 
    # Adding card to the deck
        deck.append(Card(suits_values[suit], card))

