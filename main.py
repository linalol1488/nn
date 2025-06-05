from turtle import *

shape("turtle")
penup()
colormode(255)
bgcolor("pink")
pencolor("red")
speed(200)
forward(100)
penup()
backward(50)
left(90)
pendown()
for i in range(4):
    forward(20)
    left(90)
penup()
backward(40)
pendown()
for i in range(3):
    forward(20)
    left(120)
penup()
backward(40)
pendown()
for i in range(5):
    forward(20)
    left(36)
    forward(20)
    right(108)
penup()
backward(40)
pendown()
for i in range(3):
    forward(20)
    left(120)
right(90)
for i in range(4):
    forward(20)
    left(90)
penup()
forward(40)
pendown()
circle(40)


for i in range(360):
    pencolor(i % 256, 0, i % 256)
    forward(30)
    right(90)
    fd(1)
    right(90)
    fd(30)
    left(90)
    fd(1)
    left(90)



done()