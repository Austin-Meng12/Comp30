# b_player.py

"""
title: Player class for the dice game
author: Austin Meng
date-created: 2023 - 03 - 07
"""


from a_dice import Die
class Player:
    '''


    The player for a dice_rolling game


    '''

    def __init__(self, NAME="", DICE_AMOUNT = 2):
        self.NAME = NAME
        self.DICE = []
        self.HELD_DICE = []
        for i in range(DICE_AMOUNT):
            self.DICE.append(Die())

        self.SCORE = 0
        self.TEMP_SCORE = 0


    # --- METHOD --- #
    # -- MUTATOR METHODS/SETTER METHODS -- # - Inputs, Processing
    def rollDice(self):
        for die in self.DICE:
            die.rollDie()
    
    def holdDice(self):
        print("Select a die to hold")
        for i in range(len(self.DICE)):
            print(f"{i+1}, {self.DICE[i].DIE_NUMBER}")
        DIE = int(input(">")) - 1
        self.HELD_DICE.append(self.DICE.pop(DIE))

        print("Dice Remaining: ")
        self.displayDice()
        print("Dice Held: ")

        self.displayHeldDice()

        # ask to hold more dice
        AGAIN = input("Hold more? (y/N) ")
        if AGAIN.upper() == "Y":
            return self.holdDice()

    def resetDice(self):
        self.DICE = self.HELD_DICE
        self.HELD_DICE = []


    def addScore(self, POINTS):
        self.SCORE += POINTS


    def addTempScore(self, POINTS):
        self.TEMP_SCORE += POINTS


    # -- ACCESSOR METHODS/GETTER METHODS -- # - Ouputs
    def displayDice(self):
        for i in range(len(self.DICE)):
            print(f"Die {i+1}: {self.DICE[i].DIE_NUMBER}")

    def displayScore(self):
        print(f"Score: {self.SCORE}")


    def displayHeldDice(self):
        for i in range(len(self.HELD_DICE)):
            print(F"Die {i+1}: {self.HELD_DICE[i].DIE_NUMBER}")

if __name__ == "__main__":

    PLAYER = Player()

    print("""
Welcome to Dice Roll
Get points by correctly choosing both odd, both even, or odd and even!
Lose points if you are wrong.  
    
    """)

    # --- INPUTS --- #
    print("""
1. ODD
2. EVEN
3. BOTH

    
    """)

    CHOICE = int(input(">"))

    # processing

    PLAYER.rollDice()


    if PLAYER.DICE[0].isEven() and PLAYER.DICE[1].isEven():
        RESULT = 2
    elif not PLAYER.DICE[0].isEven() and not PLAYER.DICE[1].isEven():
        RESULT = 2
    else:
        RESULT = 3


    if CHOICE == RESULT:

        PLAYER.addScore(10)

    else:

        PLAYER.addScore(-5)

    # --- OUTPUTS --- #

    PLAYER.displayDice()


    if CHOICE == RESULT:
        print("Right On!")
    else:
        print("Better Luck Next Time!")
    
    PLAYER.displayScore()

