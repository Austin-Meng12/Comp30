# a_dice.py in a_dice_game
"""
title: Die Class for Dice
author: Micheal Zhang
date-created: 2023-03-07

"""
from random import randint
class Die:
    """
    Create die objects to roll for random numbers

    """

    def __init__(self, HIGHEST_NUMBER = 6):
        # constructor for the object
        self.DIE_MAX_NUMBER = HIGHEST_NUMBER       
        self.DIE_NUMBER = 0



    def rollDie(self):
        """
        randomly roll a number for a self.DIE_NUMBER
        :return: none
    
        """
        self.DIE_NUMBER = randint(1,self.DIE_MAX_NUMBER)
    def isEven(self):
        """
        check if the rolled number is even
        :return: bool

        """
        if self.DIE_NUMBER % 2 == 0:
            return True
        else:
            return False
        

if __name__ == "__main__":
    ### VARIABLES ###
    Score = 0


    Die_1 = Die()
    Die_2 = Die()

    print("""
Welcome to Dice Roll
Get points by correctly choosing both odd, both even, or odd and even. Lose points if you are wrong
    
    """)
    while True:
    # ---INPUTS---#
        print("""
1. Guess dice will be odd
2. Guess dice will be even
3. Guess dice will be odd and even
        
        """)

        CHOICE = int(input(">"))
        # --- porcessing --- #
        Die_1.rollDie()
        Die_2.rollDie()


        if Die_1.isEven() and Die_2.isEven():
            RESULT = 2
        elif not Die_1.isEven and not Die_2.isEven():
            RESULT = 1
        else:
            RESULT = 3

        if CHOICE == RESULT:
            Score += 10
        else:
            Score -= 5
        

        # --- OUTPUT --- #

        print(f"Die 1: {Die_1.DIE_NUMBER}")
        print(f"Die 2: {Die_2.DIE_NUMBER}")


        if CHOICE == RESULT:
            print("Right On!")
        
        else:
            print("Better Luck Next Time")


        print(f"Score: {Score}")
        AGAIN = input("keep going? (Y/n)")
        if AGAIN == "" or AGAIN.upper() == "Y":
            pass
        else:
            exit()

            











    '''
    DIE1 = Die()  # instantiating the object from the class
    #print(DIE1.DIE_NUMBER)
    #print(DIE1.DIE_MAX_NUMBER)
    DIE2 = Die()
    DIE1.rollDie()
    DIE2.rollDie()



    print("die 1",DIE1.DIE_NUMBER)
    print("die 2",DIE2.DIE_NUMBER)
'''
'''
DICE = []
# create the dice
for i in range(6):
    DICE.append(Die())
# roll the dice
for i in range(6):
    DICE[i].rollDie()
    if DICE[i].isEven():
        print(f"Die {i+1} : {DICE[i].DIE_NUMBER} and is Even!")
    else:
        print(f"Die {i+1} : {DICE[i].DIE_NUMBER} and is Odd!")
'''


