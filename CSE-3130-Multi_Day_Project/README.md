# CSE-3130-Multi_Day_Project

## Discription of Brick Breaker

Brick Breaker is an arcade style game where the goal of the game is to destroy all the bricks on screen and earn points. But some bricks have different amount of health, meaning it takes more hits from the ball to destroy it. In addition, you can't hit the bottom of the screen or you will lose a life, and if you have zero lives, you lose. To prevent the brick from hitting the bottom of the screen, you control a paddle using AD (which moves it left and right). Each Brick has different colors, and whenever the ball hits the brick the color changes to a lighter shade of a color. 
There are two levels, each with very different brick layouts. The only way to win is to destroy all the bricks on the first level and the second level.
The First level is a 4X6 rectangle
the Second Level is a upside down pyramid


## Controls
The Game starts whenever you press the Space Bar, which makes the ball start to move and puts all the Text off screen expect for the SCORE and LIVES Text
The Paddle can be moved by the keybinds "A" and "D", which moves the paddle left and right respectivily.

## Features
The First Feature is how the bricks can have different health, which results in the ball needing more hits to remove. In addition, each brick has a different color depending on the amount of health it has, usually as the brick health decreases the color becomes ligther

The second Feature is Player Lives. As the ball goes out of the bottom of the screen, you lose 1 life.
Each level has a different amount of lives. After the ball goes out of bounds, the ball will automatically teleport to above the paddle. After you lose all your lives, you lose the game


## Reflection
I think this project went really well. Getting the player to move left and right was easy and getting the ball to bounce around on its own was a bit harder but didn't take that long. Plus, getting the bricks in the same list to get different X-VALUES, when displayed was kinda annoying. When I created the bricks, i created each layer individuals as different lists instead of making one big list for all the bricks. Doing each layer individuals took up tons of lines of code. I'm pretty sure there was an easier way of creating the bricks like using 1 list for all the bricks in the first level instead of 4, but I kinda got lazy so I didn't bother. Although it took up tons of lines, most if it was just repeated the same thing, which wasn't the worst for me. The only benefit to doing multiple lists for the bricks was that, it was easier to make each layer extremely distinct. For example, using multiple lists made my upside down pyramid possible. It also made it easier to manipulate and make each layer Unique. The hardest part of this entire program was the collisions. The collisions with the Window Boundaries wasn't hard, and neither was the collisions with the paddle. The collisions with the brick killed me. I spend like 5 days trying to figure it out, and every time I ended up with the ball bouncing the wrong direction or the ball completely going through the bricks. But once I drew it out, and completely B.S. my way through, the collisions worked. I'm pretty sure there are still bugs with the collisions, like the ball hitting the cornors of the brick and completely going in the wrong direction, but that rare. I didn't bother trying to fix it because by then I have already lost my mind.

The winning screen and losing screen, was also kinda annoying, but after trying a few times where I just moved everything on and off the screen ( This didn't work, there were functions blocking the paddle and ball from moving off screen), I realized I could just make a new Screen displaying everything.
The UML table and Flowchart were relativily easy to do. But on the flowchart i sometimes couldn't decide whether or not I should use a rectangle or paralelogram for some of them.

My extenstions/ extra features were also pretty easy to make.  



