# coding: utf-8
# draw a square
import turtle

turtle.shape('turtle')
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# draw a circle
import turtle

turtle.shape('turtle')
for i in range(360):
    turtle.forward(1)
    turtle.right(1)

# draw 10 inserted squares
import turtle

#turtle.shape('turtle') option, but making the movement slow
n = 0
r = 0
for i in range(10):
    for j in range(4):
        turtle.forward(n)
        turtle.right(90)
    
    turtle.penup()
    turtle.goto(-r, r)
    turtle.pendown()
    n += 20
    r += 10


# draw a spider with n foots
import turtle

turtle.shape('turtle')
n = int(input())
for i in range(n): 
    turtle.forward(200)
    turtle.stamp()
    turtle.right(360 // n)
    turtle.forward(200)
    turtle.right(180 + 360 / n)


# draw a spiral
import turtle

turtle.shape('turtle')
n = 0
for i in range(360):
    turtle.forward(n)
    turtle.right(10)
    n += 0.03


# draw a square spiral
import turtle

turtle.shape('turtle')
n = 1
for i in range(10):
    turtle.forward(n)
    turtle.right(90)
    turtle.forward(n)
    turtle.right(90)
    n += 10
    turtle.forward(n)
    turtle.right(90)
    turtle.forward(n)
    turtle.right(90)
    n += 10

# draw 10 inserted polygons
def poligon(n, rebro):
    import math
    import turtle

    turtle.left(90 / n)
    Radius = rebro / (2 * (math.sin(math.pi / n)))
    step = 0
    for i in range(10):
        for j in range(n):
            turtle.forward(rebro)
            turtle.right(360 / n)
        turtle.up()
        step -= 20
        turtle.goto(step, 0)
        turtle.down()
        n += 1
        rebro = 2 * (Radius + abs(step)) * math.sin(math.pi / n) 
        turtle.left(180 / (n - 1) - 180 / n)
    return n, rebro

n = 3
rebro = 50
poligon(n, rebro)

# draw a flour by circles 
def fleure(n):
    import turtle
    turtle.shape('turtle')
    for j in range(n):
        for i in range(360):
            turtle.forward(1.5)
            turtle.right(1)
        turtle.left(360 / n)
    return n
n = int(input())
fleure(n)


# draw a buterfly by circles
def papion(Nb_rings):
    import turtle
    R = 10
    turtle.shape('turtle')
    turtle.right(90)
    for i in range(Nb_rings):
        turtle.circle(R)
        turtle.circle(-R)
        R += 10

papion(int(input())   

# draw a spring
def spiral(Nb_turns):
    import turtle
    Big_turn = 0.5
    Small_turn = 0.1
    turtle.shape('turtle')
    turtle.left(90)

    for j in range(Nb_turns):
        for i in range(180):
            turtle.forward(Big_turn)
            turtle.right(1)
        for i in range(180):
            turtle.forward(Small_turn)
            turtle.right(1)

spiral(int(input()))            


# draw a nice smile 
import turtle

turtle.begin_fill()
turtle.color('yellow')
turtle.down()
turtle.circle(100)
turtle.end_fill()
turtle.goto(-40, 100)
turtle.begin_fill()
turtle.color('blue')
turtle.down()
turtle.circle(15)
turtle.end_fill()
turtle.up()
turtle.goto(40, 100)
turtle.down()
turtle.begin_fill()
turtle.color('blue')
turtle.down()
turtle.circle(15)
turtle.end_fill()
turtle.up()
turtle.goto(0, 100)
turtle.down()
turtle.right(90)
turtle.width(8)
turtle.color('green')
turtle.forward(40)
turtle.up()
turtle.goto(-35, 50)
turtle.down()
turtle.left(45) 
turtle.width(16) 
turtle.down() 
turtle.color('red') 
turtle.circle(50, 90) 
turtle.up()
turtle.goto(-100, 0)


# Draw a star 
def star_5(n):
    import turtle
    N = 200
    for i in range(n):
        turtle.forward(N)
        turtle.right(180  + 180 / 5)
    return n
n = 5
star_5(n)

