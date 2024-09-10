from ball import Ball
from bricks import Brick
from window import Window
from text import Text
import pygame
"""
Brick Break Game Class

"""

class Engine:

    def __init__(self):
        self.__TITLE_SCREEN = True
        # START SCREEN
        self.__WINDOW = Window("Brick Break")

        self.__TITLE = Text("Brick Break")  # The Title of the Game
        self.__TITLE.setPos((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2 -50,
                             self.__WINDOW.getHeight()//2 - self.__TITLE.getHeight()//2 ))
        self.__TITLE.setFontSize(50)
        self.__TITLE.setColor((255,30,45))  # Red Color

        # The second Title tells the Player to press enter to begin the game
        self.__TITLE_2 = Text("Press SPACE to Start")

        self.__TITLE_2.setPos((self.__WINDOW.getWidth()//2 - self.__TITLE_2.getWidth()//2 +50,
                               self.__WINDOW.getHeight() - self.__TITLE_2.getHeight()//2 - 230

                               ))
        self.__TITLE_2.setFontSize(24)




        # The Level Text, which displays the Level
        self.__LEVEL = 1
        self.__TITLE_LEVEL = Text(f"Level {self.__LEVEL}")
        self.__TITLE_LEVEL.setPos((self.__WINDOW.getWidth()//2 - self.__TITLE_LEVEL.getWidth() + 40, self.__WINDOW.getHeight() - self.__TITLE_LEVEL.getHeight()//2 -200))



        # Score Text
        self.__SCORE = 0

        self.__SCORE_TEXT = Text(f"SCORE: {self.getScore()}")
        self.__SCORE_TEXT.setPos((self.__WINDOW.getWidth()- self.__SCORE_TEXT.getWidth() - 50, 0))


        # LIVES TEXT
        self.__LIVES = 5
        self.__LIVES_TEXT = Text(f"LIVES: {self.__LIVES}")
        self.__LIVES_TEXT.setPos((0, 0))

        # The Brick your Moving (Located at the bottom of the screen)
        self.__PLAYER = Brick(15,125)
        self.__PLAYER.setPos(
            (
                self.__WINDOW.getWidth() // 2 - self.__PLAYER.getWidth() // 2,
                self.__WINDOW.getHeight() - 100

            )

        )
        self.__PLAYER.setColor((255,40,40))  #  RED


        # The ball the bounces around
        self.__BALL = Ball(10,10)
        self.__BALL.setColor((255,255,255))  # WHITE
        self.__BALL.setPos((
            self.__WINDOW.getWidth() // 2 - self.__BALL.getWidth()//2 ,
            self.__WINDOW.getHeight()  - 130
            , 30)) # located on top of the player brick
        self.__BALL.setSpeed(7)
        # The bricks that you create  (This is for the first level)


        self.__NUMBER_OF_BRICKS = 0
        self.__NUMBER_LEVEL_TWO_BRICKS = 0

        self.__BRICK = []  # This is the First Layer
        self.__BRICK_START_X = 80  # Starting X Value for the brick
        self.__BRICK_START_Y = self.__TITLE_2.getHeight() + 50 # Starting Y value for the brick
        self.__BRICK_2 = [] # second Layer
        self.__BRICK_3 = [] # Third Layer
        self.__BRICK_4 = [] # Forth Layer

        #Creating Each Layer (First LEVEL)
        for i in range(6):
            self.__BRICK.append(Brick(30,100))
            self.__NUMBER_OF_BRICKS += 1
        for brick in self.__BRICK:
            brick.setBrickHealth(4)
            brick.setColor((71, 60, 139))
            brick.setBrickPos(self.__BRICK_START_X, self.__BRICK_START_Y)
            self.__BRICK_START_X += 5 + brick.getWidth()
        self.__BRICK_START_Y += self.__BRICK[0].getHeight() + 15

        self.__BRICK_START_X = 80
        for i in range(6):
            self.__BRICK_2.append(Brick(30,100))
            self.__NUMBER_OF_BRICKS += 1
        for brick in self.__BRICK_2:
            brick.setBrickHealth(3)
            brick.setColor((16,78,139))
            brick.setBrickPos(self.__BRICK_START_X, self.__BRICK_START_Y)
            self.__BRICK_START_X += 5 + brick.getWidth()
        self.__BRICK_START_Y += self.__BRICK_2[0].getHeight() + 20



        self.__BRICK_START_X = 80
        for i in range(6):
            self.__BRICK_3.append(Brick(30,100))
            self.__NUMBER_OF_BRICKS += 1
        for brick in self.__BRICK_3:
            brick.setBrickHealth(2)
            brick.setColor((24, 116, 205))
            brick.setBrickPos(self.__BRICK_START_X, self.__BRICK_START_Y)
            self.__BRICK_START_X += 5 + brick.getWidth()
        self.__BRICK_START_Y += self.__BRICK_3[0].getHeight() + 20

        self.__BRICK_START_X = 80
        for i in range(6):
            self.__BRICK_4.append(Brick(30,100))
            self.__NUMBER_OF_BRICKS += 1
        for brick in self.__BRICK_4:
            brick.setBrickHealth(1)
            brick.setColor((0, 191, 255))
            brick.setBrickPos(self.__BRICK_START_X, self.__BRICK_START_Y)
            self.__BRICK_START_X += 5 + brick.getWidth()
        self.__BRICK_START_Y += self.__BRICK_4[0].getHeight() + 10





         ##This is for the Second level, the shape of the bricks is a pyramid

        self.__BRICK_21 = []  # First Layer
        for i in range(7):
             self.__NUMBER_LEVEL_TWO_BRICKS +=1
             self.__BRICK_21.append(Brick(10,100))

        for brick in self.__BRICK_21:
                brick.setBrickPos(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                brick.setBrickHealth(4)
                brick.setColor((139, 0, 0))
        self.__BRICK_22 = [] # Second Layer
        for i in range(5):
            self.__NUMBER_LEVEL_TWO_BRICKS += 1
            self.__BRICK_22.append((Brick(13, 110)))
        for brick in self.__BRICK_22:
            brick.setBrickPos(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
            brick.setBrickHealth(4)
            brick.setColor((139, 0, 0))

        self.__BRICK_23 = []  # Third Layer
        for i in range(5):
            self.__NUMBER_LEVEL_TWO_BRICKS += 1
            self.__BRICK_23.append(Brick(10,100))
        for brick in self.__BRICK_23:
            brick.setBrickPos(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
            brick.setBrickHealth(4)
            brick.setColor((139,0,0))
        self.__BRICK_24 = []  # Fourth Layer
        for i in range(4):
            self.__NUMBER_LEVEL_TWO_BRICKS += 1
            self.__BRICK_24.append(Brick(10,100))
        for brick in self.__BRICK_24:
            brick.setBrickPos(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
            brick.setBrickHealth(4)
            brick.setColor((139, 0, 0))
        self.__BRICK_25 = []  # Fifith Layer
        for i in range(3):
            self.__NUMBER_LEVEL_TWO_BRICKS += 1
            self.__BRICK_25.append(Brick(10,100))
        for brick in self.__BRICK_25:
            brick.setBrickPos(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
            brick.setBrickHealth(4)
            brick.setColor((139, 0, 0))

        self.__BRICK_26 = []  # Sixth Layer
        for i in range(1):
            self.__NUMBER_LEVEL_TWO_BRICKS += 1
            self.__BRICK_26.append(Brick(10,120))
        for brick in self.__BRICK_26:
            brick.setBrickPos(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
            brick.setBrickHealth(4)
            brick.setColor((139, 0, 0))
    def run(self):
        """
        The Main Function of the game, makes the entire game run
        :return:
        """

        while True:
            ### inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            PRESSED_KEYS = pygame.key.get_pressed()
            if PRESSED_KEYS[pygame.K_SPACE]: # Press enter to start the game
                self.__TITLE_SCREEN = False




            if self.__TITLE_SCREEN == False: # Start of the game
                # PLAYER movement
                self.__PLAYER.setSpeed(10)
                self.__PLAYER.moveWASD(PRESSED_KEYS)
                self.__PLAYER.checkBoundaries(
                    self.__WINDOW.getWidth(),
                    self.__WINDOW.getHeight(),
                    0,
                    self.__TITLE.getHeight()
                )
                # Ball Movement around the screen
                self.__BALL.BallMovement(self.__WINDOW.getWidth(), self.__WINDOW.getHeight(),0, self.__SCORE_TEXT.getHeight())

                # Moving all the titiles off screen
                self.__TITLE.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
                self.__TITLE_2.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
                self.__TITLE_LEVEL.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))

            if self.__BALL._OUT_OF_BOUNDS == True:  # The ball leaves the very bottom of the screen

                self.LoseLive()
                self.__BALL.setDIRX()
                if self.__LIVES < 0:
                    self.__LIVES  = 0
                self.__LIVES_TEXT = Text(f"LIVES: {self.__LIVES}")
                self.__LIVES_TEXT.setPos((0, 0))
                self.__BALL.setPos((self.__PLAYER.getX() + self.__PLAYER.getWidth()//2, self.__PLAYER.getY() - 200))
                self.__BALL.BallMovement(self.__WINDOW.getWidth(), self.__WINDOW.getHeight(), 0,
                                         self.__SCORE_TEXT.getHeight())
                self.__BALL._OUT_OF_BOUNDS = False

            if self.__LIVES <= 0:  # If you have no more Lives, show the losing screen
                self.__setLosingScreen()


            if self.__NUMBER_OF_BRICKS <= 0: # Checks if there is no more Level 1 Bricks on the Window
                # If there isnt The Level Changes
                self.addLevel()

                if self.__LEVEL == 2:

                    self.__init__()
                    self.setLives(3)
                    self.addLevel()

                    self.__BALL.setSpeed(8)

                    self.__TITLE_LEVEL = Text(f"Level {self.__LEVEL}")
                    self.__TITLE_LEVEL.setPos((self.__WINDOW.getWidth() // 2 - self.__TITLE_LEVEL.getWidth() + 40,
                                           self.__WINDOW.getHeight() - self.__TITLE_LEVEL.getHeight() // 2 - 200))
                    self.__LIVES_TEXT = Text(f"LIVES: {self.__LIVES}")
                    self.__LIVES_TEXT.setPos((0,0))

                    X = 30  # THE START OF THE SECOND LAYER, Displaying all the second level Brick
                    for brick in self.__BRICK_21:
                        brick.setBrickPos(X, self.__TITLE_2.getHeight() + 50)
                        X += 10 + brick.getWidth()

                    X = 100
                    for brick in self.__BRICK_22:
                        brick.setBrickPos(X, self.__BRICK_21[0].getY() + self.__BRICK_21[0].getHeight() + 10)
                        X += 10 + brick.getWidth()

                    X = 130
                    for brick in self.__BRICK_23:
                        brick.setBrickPos(X, self.__BRICK_22[0].getY() + self.__BRICK_22[0].getHeight() + 10)
                        X += 10 + brick.getWidth()

                    X = 200
                    for brick in self.__BRICK_24:
                        brick.setBrickPos(X, self.__BRICK_23[0].getY() + self.__BRICK_23[0].getHeight() + 10)
                        X += 10 + brick.getWidth()
                    X = 260
                    for brick in self.__BRICK_25:
                        brick.setBrickPos(X, self.__BRICK_24[0].getY() + self.__BRICK_24[0].getHeight() + 10)
                        X += 10 + brick.getWidth()
                    X = 360
                    for brick in self.__BRICK_26:
                        brick.setBrickPos(X, self.__BRICK_25[0].getY()  + self.__BRICK_25[0].getHeight() + 10)
                        X += 10 + brick.getWidth()

                    # All the First Level Brick are set to off screen
                    for brick in self.__BRICK:
                        brick.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
                    for brick in self.__BRICK_2:
                        brick.setPos((self.__WINDOW.getWidth(),self.__WINDOW.getHeight()))
                    for brick in self.__BRICK_3:
                        brick.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))
                    for brick in self.__BRICK_4:
                        brick.setPos((self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))



            # Checks whether or not their are no more bricks on the second layer, if there isnt, display the winning screen
            if self.__NUMBER_LEVEL_TWO_BRICKS <= 0:
                self.__setWinningScreen()



           ### COLLISIONS IN THE GAME

            # Collision with the paddle
            if self.__BALL.BallPaddleCollision(self.__PLAYER.getPos(), self.__PLAYER.getDimensions()):
                    self.__BALL._DIR_Y = - 1


            # Brick Collision  for the first layer
            for brick in self.__BRICK:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((0,191,255),(24,116,205),(16,78,139))
                    if brick._BRICK_DEAD == True:

                        self.removeFirstLevelBrick(self.__BRICK, brick)
            for brick in self.__BRICK_2:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((0,191,255),(24,116,205),(16,78,139))
                    if brick._BRICK_DEAD == True:

                        self.removeFirstLevelBrick(self.__BRICK_2, brick)

            for brick in self.__BRICK_3:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((0,191,255),(24,116,205),(16,78,139))
                    if brick._BRICK_DEAD == True:

                        self.removeFirstLevelBrick(self.__BRICK_3, brick)

            for brick in self.__BRICK_4:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((0,191,255),(24,116,205),(16,78,139))
                    if brick._BRICK_DEAD == True:

                        self.removeFirstLevelBrick(self.__BRICK_4, brick)







            # Brick Collision for the second layer

            for brick in self.__BRICK_21:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())

                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((255,215,0),(255,125,64),(205,16,118))
                    if brick._BRICK_DEAD == True:
                        self.removeFirstLevelBrick(self.__BRICK_21, brick)

            for brick in self.__BRICK_22:
                if self.__BALL.BALLBRICKCollision(brick.getPos(),brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((255,215,0),(255,125,64),(205,16,118))
                    if brick._BRICK_DEAD == True:
                        self.removeFirstLevelBrick(self.__BRICK_22, brick)


            for brick in self.__BRICK_23:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((255, 215, 0), (255, 125, 64), (205, 16, 118))
                    if brick._BRICK_DEAD == True:
                        self.removeFirstLevelBrick(self.__BRICK_23, brick)
            for brick in self.__BRICK_24:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((255, 215, 0), (255, 125, 64), (205, 16, 118))
                    if brick._BRICK_DEAD == True:
                        self.removeFirstLevelBrick(self.__BRICK_24, brick)
            for brick in self.__BRICK_25:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((255, 215, 0), (255, 125, 64), (205, 16, 118))
                    if brick._BRICK_DEAD == True:
                        self.removeFirstLevelBrick(self.__BRICK_25, brick)
            for brick in self.__BRICK_26:
                if self.__BALL.BALLBRICKCollision(brick.getPos(), brick.getDimensions()):
                    self.__BALL.determineBoxDirection(brick.getPos(), brick.getDimensions())
                    brick.LoseHealth()
                    brick.DetermineBrickHealthColor((255, 215, 0), (255, 125, 64), (205, 16, 118))
                    if brick._BRICK_DEAD == True:
                        self.removeFirstLevelBrick(self.__BRICK_26, brick)

            # OUTPUT
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPos())
            self.__WINDOW.getSurface().blit(self.__TITLE_2.getSurface(), self.__TITLE_2.getPos())
            self.__WINDOW.getSurface().blit(self.__TITLE_LEVEL.getSurface(), self.__TITLE_LEVEL.getPos())
            self.__WINDOW.getSurface().blit(self.__SCORE_TEXT.getSurface(), self.__SCORE_TEXT.getPos())
            self.__WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPos())
            self.__WINDOW.getSurface().blit(self.__PLAYER.getSurface(), self.__PLAYER.getPos())
            self.__WINDOW.getSurface().blit(self.__LIVES_TEXT.getSurface(), self.__LIVES_TEXT.getPos())

            for brick in self.__BRICK:
              self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_2:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_3:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_4:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())

            for brick in self.__BRICK_21:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_22:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_23:
                 self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_24:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_25:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())
            for brick in self.__BRICK_26:
                self.__WINDOW.getSurface().blit(brick.getSurface(), brick.getPos())

            self.__WINDOW.updateFrame()




    def removeFirstLevelBrick(self,LIST,BRICK):
        """
        After it collides, it loses health, or removes the brick (First Layer)
        :param LIST: BRICK_LIST
        :param BRICK:
        :return:
        """
        self.__NUMBER_OF_BRICKS -= 1
        LIST.remove(BRICK)
        self.addScore()
        self.__SCORE_TEXT = Text(f"SCORE: {self.getScore()}")
        self.__SCORE_TEXT.setPos((
            self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 0
        ))
    def removeSecondLevelBrick(self,LIST, BRICK):
        """
        After it collides, it loses it health, or removes the brick (Second Layer)
        :param LIST:
        :param BRICK:
        :return:
        """
        self.__NUMBER_LEVEL_TWO_BRICKS -= 1
        LIST.remove(BRICK)
        self.addScore()
        self.__SCORE_TEXT = Text(f"SCORE: {self.getScore()}")

        self.__SCORE_TEXT.setPos(
        (
            self.__WINDOW.getWidth() - self.__SCORE_TEXT.getWidth() - 20, 0
        )

    )
        #Accessor
    def getLevel(self):
        """

        :return: int
        """
        return self.__LEVEL

    def getScore(self):
        """

        :return: int
        """
        return self.__SCORE
    #Modifier
    def addLevel(self):
        """
        Adds A level
        :return:
        """
        self.__LEVEL += 1
    def addScore(self):
        """
        Add 1 after it collides with a brick
        :return:
        """
        self.__SCORE += 1
    def LoseLive(self):
        self.__LIVES -= 1

    def setLives(self,LIVES):
        """

        :param LIVES: Int
        :return:
        """

        self.__LIVES = LIVES

    def __setLosingScreen(self):
        """
        After the Player has zero lives, display this
        :return:
        """
        while True:
            ### inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.__LOSING_TITLE = Text("YOU LOST")
            self.__LOSING_TITLE.setPos((self.__WINDOW.getWidth() // 2 - self.__LOSING_TITLE.getWidth() // 2,
                                       self.__WINDOW.getHeight() // 2 - self.__LOSING_TITLE.getHeight() // 2))

            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__LOSING_TITLE.getSurface(), self.__LOSING_TITLE.getPos())
            self.__WINDOW.updateFrame()

            self.__BALL.setSpeed(0)



    def __setWinningScreen(self):
        """
                Winning Screen after the player clears out all the bricks for each level
                :return:
        """
        while True:
            ### inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.__WINNING_TEXT = Text("GOOD JOB, YOU WON")
            self.__WINNING_TEXT.setPos((self.__WINDOW.getWidth() // 2 - self.__WINNING_TEXT.getHeight() // 2,
                                       self.__WINDOW.getHeight() // 2 - self.__WINNING_TEXT.getHeight() // 2))
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__WINNING_TEXT.getSurface(), self.__WINNING_TEXT.getPos())
            self.__WINDOW.updateFrame()







if __name__ == "__main__":

    pygame.init()
    GAME = Engine()
    GAME.run()