# main.py

"""
title: Main file to run for the program
author: Austin Meng
date-created: 2023 - 03 -08

"""
"""
The main file is not required, however, many languages require a file titled "main" to indicate that it is the 
the starting file for the program. While python does not require this file, most C based languages
(Java, C#, C++) require a main file to compile the project


"""
from c_simple_game import Game

def main():
    GAME = Game()
    GAME.run()

if __name__ == "__main__":
    main()




