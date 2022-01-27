#director
from pickle import TRUE
from turtle import clear
from card import Card

import random
import os

# the director will control the game and keep score. 
class Director:

    def __init__(self):
    #arguments
        self.is_playing= TRUE
        self.deck= []
        self.cards=[]
        self.cards_values={}
        self.suit=[]
        self.suits_values={}
        self.score=300

    def start_game(self):
        while self.is_playing:
            self.clear()
            self.print_scoreboard()
            self.print_cards()
            self.hi_lo_game()

    def clear():
        os.system("clear")

    def print_scoreboard(score, chances):
        print("\t\t\t     ____________________")
        print("\t\t\t    |                    |")
        if score >= 10:
            print("\t\t\t    |     Score = {}     |".format(score))
        else:   
         print("\t\t\t    |     Score = {}      |".format(score))
        print("\t\t\t    |  Chances Left = {}  |".format(chances))  
        print("\t\t\t    |____________________|")
 
    def print_cards(prev_card, current_card):
     
        print()
        print("\t ________________      ________________      ________________")
        print("\t|                |    |                |    |                |")
        if prev_card.value == '10' and current_card.value == '10':
            print("\t|  {}            |    |  {}            |    |                |".format(prev_card.value,current_card.value))
        elif prev_card.value == '10': 
            print("\t|  {}            |    |  {}             |    |                |".format(prev_card.value,current_card.value))   
        elif current_card.value == '10':
            print("\t|  {}             |    |  {}            |    |                |".format(prev_card.value,current_card.value))   
        else:
            print("\t|  {}             |    |  {}             |    |                |".format(prev_card.value,current_card.value))  
        print("\t|                |    |                |    |      * *       |")
        print("\t|                |    |                |    |    *     *     |")
        print("\t|                |    |                |    |   *       *    |")
        print("\t|                |    |                |    |   *       *    |")
        print("\t|       {}        |    |       {}        |    |          *     |".format(prev_card.suit, current_card.suit))
        print("\t|                |    |                |    |         *      |")
        print("\t|                |    |                |    |        *       |")
        print("\t|                |    |                |    |                |")
        print("\t|                |    |                |    |                |")
        if prev_card.value == '10' and current_card.value == '10':
            print("\t|            {}  |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))
        elif prev_card.value == '10': 
            print("\t|            {}  |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))   
        elif current_card.value == '10':
            print("\t|            {}   |    |            {}  |    |        *       |".format(prev_card.value,current_card.value))   
        else:
            print("\t|            {}   |    |            {}   |    |        *       |".format(prev_card.value,current_card.value))  
        print("\t|________________|    |________________|    |________________|")
        print()


    # The card value
    cards_values = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}
 
    def hi_lo_game(deck,prev_card, current_card, cards_values):

        cards_values={} 
        global print_scoreboard
 
    # Initialize the previous card
        prev_card = Card(" ", " ")
 
    # Initialize the current card
        current_card = random.choice(deck)
 
    # The starting card cannot be lowest or highest
        while current_card.value == "A" or current_card.value == "K":
            current_card = random.choice(deck)
 
    # Remove the card from the deck 
        deck.remove(current_card)
    
    # Number of chances left
        chances = 5
    # The current/starting score
        score = 300
    
    # The GAME LOOP
        while chances:
            print_scoreboard= (score, chances)
            print_cards=(prev_card, current_card)
            print_scoreboard(score, chances)
            print_cards(prev_card, current_card)
 
            print("\t\t   ------------------------------------")
            print("\t\t\t\tGAME MENU")
            print("\t\t   ------------------------------------")
            print()
            print("\t\t      Enter 1 to bet for a high card")
            print("\t\t      Enter 0 to bet for a low card")
            print()
         
            # Check if we reached the end of the deck
            if len(deck) == 0:
                print_cards(prev_card, current_card)
            print("\t\t    YOU HAVE REACHED THE END OF THE DECK!")
            print("\t\t           Congratulations!!!")
            print()
            print("\t\t          Your Final Score =", score)
            print("\t\t        Thank you for playing!!!")
            clear()
            break
 
            # Try block for player input error
        try:
            choice = int(input("\t\t\t  Enter your choice = "))
        except ValueError:
                clear()
                print("\t\t\tWrong Input!! Try Again.")
                continue   
 
        # Some wrong choice
        if choice > 1 or choice < 0:
            clear()
            print("\t\t\tWrong Input!! Try Again.")
            continue       
 
        # Switch the current card to the previous card
        prev_card = current_card
 
        # Choose the new current card
        current_card = random.choice(deck)
 
        # Remove the new card from the deck
        deck.remove(current_card)
 
        # A high card
        if cards_values[current_card.value] > cards_values[prev_card.value]:
            result += 1
 
        # A low card    
        elif cards_values[current_card.value] < cards_values[prev_card.value]:
            result = 0
 
        # Same value card   
        else:
            result = score -75    
 
        # A Tie Round
        if result == score -75:
            clear()
            print("\t\t\t TIE GAME!! Play Again")
 
        # Round won
        elif choice == result:
            clear()
            print("\t\t\t YOU WIN!!! Play Again")
            score = score + 100  
 
        # Round Lost    
        else:
            if chances == 1:
                clear()
                print("\t\t\t\tGAME OVER")
                print_cards(prev_card, current_card)
                print("\t\t        Your Final Score =", score)
                print("\t\t      Thank you for playing!!!")  
            clear()
            print("\t\t\t YOU LOSE!! Play Again")
            chances = chances - 1
            score = score -75
 
 