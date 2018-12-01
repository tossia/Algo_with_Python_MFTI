
# coding: utf-8

# квадрат

# In[17]:


import turtle

turtle.shape('turtle')
for i in range(4):
    turtle.forward(100)
    turtle.right(90)


# круги

# In[19]:


import turtle

turtle.shape('turtle')
for i in range(360):
    turtle.forward(1)
    turtle.right(1)
for i in range(360):
    turtle.forward(1)
    turtle.left(1)


# 10 вложенных квадратов

# In[1]:


import turtle

#turtle.shape('turtle')
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


# паук с 12 лапками

# In[1]:


import turtle

turtle.shape('turtle')
for i in range(12):
    turtle.forward(200)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(200)
    turtle.right(150)


# спираль

# In[3]:


import turtle

turtle.shape('turtle')
n = 0
for i in range(360):
    turtle.forward(n)
    turtle.right(10)
    n += 0.03


# квадратная спираль

# In[7]:


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


# Нарисовать десять встроенных многоугольников через функцию

# In[1]:


import turtle
import math
turtle.shape('turtle')
M = 100
angles = 3
Nb_figure = 5
Radius = 0
Nb = 3
for j in range(Nb_figure):
    for i in range(angles):
        Radius = M / 2 * (math.sin(math.radians(360 / 2 * Nb)))
        turtle.forward(M)
        turtle.right(360 // angles)
        Nb += 1
    turtle.penup()
    Radius += 10
    turtle.goto(Radius, Radius)
    turtle.pendown()
    angles +=1


# In[ ]:


import math
Rad = math.radians(60)
print(Rad)
Radius = 100 / 2 * math.sin(math.radians(60))
print("Radius", Radius)


# Нарисовать цветок из окружностей 6 через функцию

# In[1]:


def fleure(n):
    import turtle
    turtle.shape('turtle')
    for j in range(n):
        for i in range(360):
            turtle.forward(1.5)
            turtle.right(1)
        turtle.left(360 // n)
    return n
n = int(input())
fleure(n)


# Нарисовать бабочку из окружностей через функцию

# In[23]:


def papion(Nb_rings):
    import turtle
    R = 10
    turtle.shape('turtle')
    turtle.right(90)
    for i in range(Nb_rings):
        turtle.circle(R)

        turtle.circle(-R)

        R += 10

papion(int(input()))


    


# нарисовать пружину через функцию

# In[3]:


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


# Нарисуйте смайлик с помощью написанных функций рисования круга и дуги.

# In[15]:


import turtle

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


# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами. 

# In[18]:


turtle.reset()

