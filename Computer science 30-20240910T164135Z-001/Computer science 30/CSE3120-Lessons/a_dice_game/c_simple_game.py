# c_simple_game.py


"""
title: Game class for the dice roll game
author: Austin Meng
date-created: 2023 - 03 - 08
"""

from b_player import Player


class Game:

    def __init__(self):
        # construtor is the setup of the main program code
        self.TITLE = """
       
Welcome to Dice Roll
Get points by correctly choosing both odd, both even, or odd and even!
Lose points if you are wrong.  
 
        """
        self.CHOICE = 0
        self.RESULT = 0
        self.PLAYER = Player()

        

    def run(self):
        # main program code(main loop)
        print(self.TITLE)
        while True:
            ### input
            self.menu()
            ### processing
            if self.CHOICE == 4:
                exit()
            self.PLAYER.rollDice()
            self.calcScore()
            ### output
            self.displayRESULT()
            
    def menu(self):
        print("""
1. ODD
2. EVEN
3. BOTH
4. EXIT
        
        
        
        """)

        self.CHOICE = int(input("> "))

    def calcScore(self):
        if self.PLAYER.DICE[0].isEven() and self.PLAYER.DICE[1].isEven():
            self.RESULT = 2
        elif not self.PLAYER.DICE[0].isEven() and not self.PLAYER.DICE[1].isEven():
            self.RESULT = 1
        else:
            self.RESULT = 3

        if self.CHOICE == self.RESULT:
            self.PLAYER.addScore(10)
        else:
            self.PLAYER.addScore(-5)

    def displayRESULT(self):
        self.PLAYER.displayDice()

        if self.PLAYER.displayDice():
            print("Right On!")
        else:
            print("Better Luck Next Time")

        self.PLAYER.displayScore()

if __name__ == "__main__":
    GAME = Game()
    GAME.run()

