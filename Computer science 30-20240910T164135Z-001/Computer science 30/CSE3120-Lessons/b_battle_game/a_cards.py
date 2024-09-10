'''
title: War Card Game
Author: Austin Meng
date-created: 2023 - 03 -10

'''
            
from random import randint
class Card:
    """
    Create die objects to roll for random numbers

    """

    def __init__(self, HIGHEST_NUMBER = 13):
        # constructor for the object
        self.CARD_MAX = HIGHEST_NUMBER       
        self.CARD = 0


    def randomcard(self):
        # Generates a random card from 1 to 13:

        self.CARD = randint(1,self.CARD_MAX)




if __name__ == "__main__":
   # VAraibles
   player_1 = Card()
   player_2 = Card()

   OUTPUT = player_1.randomcard()
   print(OUTPUT)

