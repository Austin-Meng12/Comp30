import pygame

class mySprite:
    """
    Many of the common attributes and methods for sprites in pygame
    """
    def __init__(self, HEIGHT=0, WIDTH=0, X=0, Y=0, SPD=0, COLOR=(255, 255, 255)):
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self._X = X
        self._Y = Y
        self._POS = (self._X, self._Y)
        self._SPD = SPD
        self._COLOR = COLOR
        self._DIR_X = 1
        self._DIR_Y = 1


    ###Movement Methods
    def marqueeX(self, MAX_WIDTH, MIN_WIDTH=0):
        """
        Not using this, just for testing
        :param MAX_WIDTH:
        :param MIN_WIDTH: 0, but is changable
        :return:
        """
        if self._X > MAX_WIDTH:
            self._X = MIN_WIDTH - self.getWidth()

        self._POS = (self._X, self._Y)
    def moveWASD(self, KEY_PRESSED):
        """
        move sprite with AD
        :param KEY_PRESSED:  List
        :return: none
        """
        if KEY_PRESSED[pygame.K_d]:
            self._X += self._SPD
        if KEY_PRESSED[pygame.K_a]:
            self._X -= self._SPD

        self._POS = (self._X, self._Y)
    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X = 0, MIN_Y=0):
        """
        Checks whether or not the player hit the boundries

        """
        if self._X > MAX_X - self.getWidth():
            self._X = MAX_X - self.getWidth()
        if self._X < MIN_X:
            self._X = MIN_X
        if self._Y > MAX_Y - self.getHeight():
            self._Y = MAX_Y - self.getHeight()
        if self._Y < MIN_Y:
            self._Y = MIN_Y


        self._POS = (self._X, self._Y)

    # Modifier
    def setWidth(self, WIDHT):
        """
        Changes the Width of the Sprite
        :param WIDHT: int
        :return:
        """
        self.__WIDTH = WIDHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        """
        Change the Height of the Sprite
        :param HEIGHT: int
        :return:
        """
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)
    def getDimensions(self): # Accessor

        """

        :return: TUPLE
        """
        return (self._SURFACE.get_width(), self._SURFACE.get_height())

    #Modifer
    def setPos(self, TUPLE):
        """
        Sets the Postion of the Sprite
        :param TUPLE:
        :return:
        """
        self._X = TUPLE[0]
        self._Y = TUPLE[1]
        self._POS = (self._X, self._Y)

    def setColor(self, TUPLE):
        """
        Set the Color of the Sprite
        :param TUPLE:
        :return:
        """
        self._COLOR = TUPLE

    def setSpeed(self, SPD):
        """
        Speed of the Sprite
        :param SPD: int
        :return:
        """
        self._SPD = SPD


    # ACCESSOR
    def getWidth(self):
        """

        :return: self._SURFACE.get_width()
        """
        return self._SURFACE.get_width()

    def getHeight(self):
        """

        :return: self._SURFACE.get_height()
        """
        return self._SURFACE.get_height()


    def getDim(self):
        """

        :return: tuple
        """
        return self._DIM

    def getPos(self):
        """

        :return: tuple
        """
        return self._POS

    def getSurface(self):
        """

        :return: self._SURFACE ---- > obj
        """
        return self._SURFACE








