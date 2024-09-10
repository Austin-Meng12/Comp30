import pygame
from my_sprite import mySprite
from text import Text
import random
from window import Window

class Brick(mySprite):
    def __init__(self, WIDTH=1, HEIGHT=1):
        mySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)
        self._BRICK_LIVES = 0
        self._BRICK_DEAD = False

    #Modifier
    def setColor(self, TUPLE):
        # polymorphs the setColor class from mySprite

        mySprite.setColor(self, TUPLE)
        self._SURFACE.fill(self._COLOR)

        # creating the ball that bounces around

    def setBrickPos(self,X,Y):
        """
        Sets the X and Y for the bricks in each individual layer
        :param X:int
        :param Y:int
        :return:
        """
        self.setPos((X ,Y))



    # ACCESSOR METHODS
    def getX(self):
        """

        :return:  int
        """
        return self._X

    def getY(self):
       """

       :return: int
       """
       return self._Y

    # MODIFIER
    def setBrickHealth(self, HEALTH):
        """
        sets the brick health for each brick
        :param HEALTH: int
        :return:
        """

        self._BRICK_LIVES = HEALTH


    def LoseHealth(self):
        """
        Lose a brick live after each hit
        :return:
        """
        self._BRICK_LIVES -= 1


    def DetermineBrickHealthColor(self, COLOR1, COLOR2, COLOR3):
        """
        After the ball hits, the brick will change color depending on the lives it has
        :param COLOR1: TUPLE
        :param COLOR2: TUPLE
        :param COLOR3: TUPLE
        :return: bool (Only when it has no lives left)
        """
        if self._BRICK_LIVES == 3:
            self.setColor(COLOR3)
        if self._BRICK_LIVES == 2:
            self.setColor(COLOR2)
        if self._BRICK_LIVES == 1:
            self.setColor(COLOR1)
        if self._BRICK_LIVES == 0:
            self._BRICK_DEAD = True







