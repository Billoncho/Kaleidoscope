# Kaleidoscope.py
# Billy Ridgeway
# Creates a kaleidoscope with 50 spirals.

import random               # Imports the random library.
import turtle               # Imports turtle library.
t = turtle.Pen()            # Creates a new turtle pen called t.
t.speed(0)                  # Sets the speed of the pen to fast.
turtle.bgcolor("black")     # Sets the background color to black.

# Creates a list of colors.
colors = ["red", "yellow", "blue", "green", "orange", "purple",
          "white", "gray"]

for n in range(50):                                         # Sets the range of n to 50.
    t.pencolor(random.choice(colors))                       # Randomly chooses the pen's color.
    size = random.randint(10, 40)                           # Randomly chooses the size of the shape.
    x = random.randrange(size, turtle.window_width()//2)    # Randomly sets the x coordinate.
    y = random.randrange(size, turtle.window_height()//2)   # Randomly sets the y coordinate.
    sides = random.randint(3, 12)                           # Randomly sets the number of side in the spiral.
    thick = random.randint(1, 6)                            # Randomly sets the thickness of the pen.
    t.pensize(thick)                                        # Sets the thickness of the pen to the variable contained in thick.
    angle = t.heading()                                     # Keeps track of the pen's direction.                        

    t.penup()                   # Stops the pen from drawing.
    t.setpos(x, y)              # Moves the pen to the new position.
    t.pendown()                 # Sets the pen to draw.
    for m in range(size):       # Sets m to the range in the variable size.
        t.forward(m*2)          # Moves the pen forward by the value m times 2.
        t.left(360/sides + 1)   # Moves the pen left by 360 degrees divided by the number of sides plus 1.
       
    t.penup()                   # Stops the pen from drawing.
    t.setpos(-x, y)             # Moves the pen to the new position.
    t.setheading(180 - angle)   # Changes the pens heading to give it a mirrored reflection effect.
    t.pendown()                 # Sets the pen to draw.
    for m in range(size):       # Sets m to the range in the variable size.
        t.forward(m*2)          # Moves the pen forward by the value m times 2.
        t.right(360/sides + 1)   # Moves the pen left by 360 degrees divided by the number of sides plus 1.

    t.penup()                   # Stops the pen from drawing.
    t.setpos(-x, -y)            # Moves the pen to the new position.
    t.setheading(angle - 180)   # Changes the pens heading to give it a mirrored reflection effect.
    t.pendown()                 # Sets the pen to draw.
    for m in range(size):       # Sets m to the range in the variable size.
        t.forward(m*2)          # Moves the pen forward by the value m times 2.
        t.left(360/sides + 1)
       
    t.penup()                   # Stops the pen from drawing.
    t.setpos(x, -y)             # Moves the pen to the new position.
    t.setheading(360 - angle)   # Changes the pens heading to give it a mirrored reflection effect.
    t.pendown()                 # Sets the pen to draw.
    for m in range(size):       # Sets m to the range in the variable size.
        t.forward(m*2)          # Moves the pen forward by the value m times 2.
        t.right(360/sides + 1)   # Moves the pen left by 360 degrees divided by the number of sides plus 1.
        
    


            
