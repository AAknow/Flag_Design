## CST-16163 Intro to Computer Programming
## By: Aaron Knowles

import turtle

t = turtle.Turtle()
t.up()
t.speed(10)

# draws initial flag border and fills it with gold for the trim
def drawBorder():
    t.goto(-300, -150)
    t.color("black", "gold")
    t.begin_fill()
    t.down()
    t.goto(300, -150)
    t.goto(300, 150)
    t.goto(-300, 150)
    t.goto(-300, -150)
    t.up()
    t.end_fill()
    drawTrim()

# draws the trim and fills the flag in with black
def drawTrim():
    t.color("black", "black")
    t.begin_fill()
    t.goto(-280, -130)
    t.down()
    t.goto(280, -130)
    t.goto(280, 130)
    t.goto(-280, 130)
    t.goto(-280, -130)
    t.end_fill()
    drawStripes()

# draws the stripes
def drawStripes():
    t.left(90)
    side = 0
    while True:
        t.color("black", "red")
        # if turtle x coordinate matches x axis of trim
        if int(round(t.xcor())) == -280 or int(round(t.xcor())) == 280:
            if side > 225 and int(round(t.xcor())) == -280:
                # swaps turtle to other side if on left side of flag
                t.up()
                t.goto(280, 130)
                t.right(180)
                side = 0
                t.down()
            elif side > 225 and int(round(t.xcor())) == 280:
                # ends the loop if right side of flag is finished
                break
            else:
                t.begin_fill()
                # adds 25 to side lengths of the right triangle
                side += 25
                t.forward(25)
                t.right(135)
                # calculates hypotenuse based on current side length
                t.forward(((side ** 2) + (side ** 2)) ** .5)
        # for the vertical borders of the trim
        else:
            # adds 25 to side lengths of the right triangle
            side += 25
            t.left(45)
            t.forward(25)
            t.left(135)
            # calculates hypotenuse based on current side length
            t.forward(((side ** 2) + (side ** 2)) ** .5)
            t.right(45)
            t.end_fill()
    drawCircle()

def drawCircle():
    # moves turtle to starting position
    t.up()
    t.goto(0, -100)
    t.left(90)
    # creates first red circle and fills in with gold
    t.down()
    t.color("red", "gold")
    t.pensize(8)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    # draws smaller black circle to better pronounce circle
    t.color("black")
    t.pensize(2)
    t.circle(100)
    drawLetters()

def drawLetters():
    # move to starting position for drawing letters
    t.up()
    t.goto(10, -10)
    t.left(90)
    t.color("black")
    t.pensize(10)
    t.down()
    turns = 4
    while True:
        # draws each side for both O and U
        for i in range(turns):
            t.forward(50)
            t.left(45)
            t.forward(10)
            t.left(45)
        # after finishing the O, move to start of U and create the top
        if turns == 4:
            t.up()
            t.left(90)
            t.forward(25)
            t.right(90)
            t.forward(25)
            t.left(90)
            t.down()
            t.forward(5)
            t.backward(10)
            t.forward(5)
            t.left(90)
        # at the end of the U, create other side of the top
        else:
            t.forward(50)
            t.left(90)
            t.forward(5)
            t.backward(10)
            t.forward(5)
            t.hideturtle()
            break
        # changes number of sides
        turns = 2
        
drawBorder()
    

