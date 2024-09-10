# ball.py in CSE-3130-multi day

"""
Title: Ball class for brick break
Author: Austin Meng
Date-created: 2023-04-25
"""
from my_sprite import mySprite
from window import Window
import pygame
import math

class Ball(mySprite):

    def __init__(self, WIDTH = 1, HEIGHT = 1):
        mySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)


        self._OUT_OF_BOUNDS = False



    def BallMovement(self, SCREEN_WIDTH_MAX, SCREEN_HEIGHT_MAX, SCREEN_WIDTH_MIN = 0, SCREEN_HEIGHT_MIN =0):
        """
        Makes the Ball Move, and checks whenever the ball hits the boundries
        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_HEIGHT_MAX: int
        :param SCREEN_WIDTH_MIN: int (default and zero but is changable)
        :param SCREEN_HEIGHT_MIN: int (default at zero but is changalbe
        :return:
        """
        while True:
            self._X += self._DIR_X * self._SPD
            self._Y += self._DIR_Y * self._SPD

            if self._X > SCREEN_WIDTH_MAX - self.getWidth():
                self._DIR_X = -1

            if self._X < SCREEN_WIDTH_MIN:
                self._DIR_X = 1

            if self._Y > SCREEN_HEIGHT_MAX - self.getHeight():
               self._OUT_OF_BOUNDS = True

            if self._Y < SCREEN_HEIGHT_MIN:
                self._DIR_Y = 1

            self._POS = (self._X, self._Y)

            break

    def BallPaddleCollision(self,POSITION, DIMENSION):
        """
                Check if a sprite is colliding with the current sprite
                :param POSITION: tuple
                :param DIMENSION: tuple
                :return: bool
                """
        SPRITE_X = POSITION[0]
        SPRITE_Y = POSITION[1]
        SPRITE_W = DIMENSION[0]
        SPRITE_H = DIMENSION[1]
        if SPRITE_X >= self._X - SPRITE_W and SPRITE_X <= self._X + self.getWidth():

            if SPRITE_Y >= self._Y - SPRITE_H and SPRITE_Y <= self._Y + self.getHeight():
                return True

        return False

    def BALLBRICKCollision(self,POSITION, DIMENSION):
        """
                Check if a sprite is colliding with the current sprite
                :param POSITION: tuple
                :param DIMENSION: tuple
                :return: bool
                """
        SPRITE_X = POSITION[0]
        SPRITE_Y = POSITION[1]
        SPRITE_W = DIMENSION[0]
        SPRITE_H = DIMENSION[1]

        if SPRITE_X >= self._X - SPRITE_W and SPRITE_X <= self._X + self.getWidth():


                if SPRITE_Y >= self._Y - SPRITE_H and SPRITE_Y <= self._Y + self.getHeight():
                    return True


        return False


    def determineBoxDirection(self,POSITION, DIMENSION):
        """
        This is for determining the direction of the Ball after it collides with one of the bricks
        POSITION - means the X and Y coords of the brick its colliding with
        DIMENSION - means the Width and Height of the brick

        :param POSITION: TUPLE
        :param DIMENSION: TUPLE
        :return:
        """

        SPRITE_X  = POSITION[0]
        SPRITE_Y = POSITION[1]
        SPRITE_W = DIMENSION[0]
        SPRITE_H = DIMENSION[1]

        if SPRITE_X < self._X + self.getWidth() < SPRITE_X + SPRITE_W + 10 and self._Y + self.getHeight() > SPRITE_Y + SPRITE_H:
           self.setDIRY()   #Bottom
        if SPRITE_X < self._X +  self.getWidth() < SPRITE_X +  SPRITE_W + 10 and self._Y < SPRITE_Y:
           self.setDIRY()       # Top
        if SPRITE_Y < self._Y + self.getHeight() < SPRITE_Y + SPRITE_H + 10 and self._X + self.getWidth() > SPRITE_X + SPRITE_W:
           self.setDIRX()    # Right
        if SPRITE_Y < self._Y + self.getHeight() < SPRITE_Y + SPRITE_H + 10 and self._X - 10 < SPRITE_X:
            self.setDIRX()   # Left

    #MODIFIER
    def setDIRY(self):
        """
        The Y Direction changes (Goes in the opposite direction)
        :return:
        """
        self._DIR_Y = self._DIR_Y * -1


    def setDIRX(self):
        """
        The X DIrection changes (goes in the opposite direction)
        :return:
        """
        self._DIR_X = self._DIR_X * -1
















































if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("Ball Class")
    BALL = Ball(50,50)
    BALL.setColor((255,255,255))
    BALL.setPos((500,500))




    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        # Outputs
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPos())
        WINDOW.updateFrame()


