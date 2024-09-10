# d_farkle.py
'''
titile: Farkle Game
author: Ausitn Meng
date-created: 2023 - 03 - 08
'''

from b_player import Player
class Game:
    def __init__(self):
        self.PLAYER = []
        self.setPlayers()
        self.GAME_OVER = False

    def run(self):
        while not self.GAME_OVER:
            self.turn()

    def setPlayers(self):
        PLAYER_NUM = int(input("How many Players?"))
        for i in range(PLAYER_NUM):
            NAME = input("Name: ")
            self.PLAYER.append(Player(NAME, 6))

    def turn(self):
        for player in self.PLAYER:
            print(f"{player.NAME}'s turn.")
            for i in range(3):
                player.rollDice()
                player.holdDice()
                
                if input("keep Rolling? (Y/n) ").upper() == "N":
                    break

            player.addScore(int(input("Points: ")))     
        for player in self.PLAYER:
            if player.SCORE > 10000:
                self.GAME_OVER = True

if __name__ == "__main__":
    GAME = Game()
    GAME.run()


