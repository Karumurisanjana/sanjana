from turtle import *
import turtle as tur
import random
import time

t = tur.Turtle()
tur.title("Pythontpoint")
t.speed(6)

tur.bgcolor("black")
t.color("red")
t.pensize(5)

t.left(60)
t.fd(50)
t.left(15)
t.circle(100, 90)
t.fd(30)
t.pensize(10)
t.penup()
t.right(90)
t.fd(20)
t.pendown()

t.right(40)
t.circle(-50, 90)
t.fd(20)
t.left(150)

# second head curve
t.color("red")
t.penup()
t.fd(40)
t.left(20)
t.pendown()
t.circle(50, 90)

# third head curve

# goto beginning
t.color("red")
t.penup()
t.goto(0, 0)  # Fixed the goto function here
t.pensize(5)
t.pendown()
t.left(30)
t.fd(120)
t.circle(60, 270)

# eyes
t.color("silver")
t.penup()
t.forward(30)
t.right(50)
t.forward(135)
t.pendown()
t.pensize(8)
t.circle(50, 90)
t.left(95)
t.penup()
t.circle(60, 75)

# eyebrows
t.penup()
t.forward(15)
t.left(90)
t.pensize(2)
t.pendown()
t.circle(70, 90)

# ears
t.pensize(5)
t.penup()
t.forward(75)
t.right(90)
t.forward(20)
t.pendown()
t.circle(90, 90)
t.forward(20)

t.circle(30, 170)
t.right(180)
t.circle(28, 180)
t.right(160)
t.circle(25, 180)
t.right(160)
t.circle(22, 160)
t.forward(20)
t.circle(60, 45)

# trunk

t.penup()
t.goto(0, 0)  # Fixed the goto function here
t.left(130)
t.fd(140)
t.right(250)
t.backward(20)
t.circle(80, 20)
t.circle(20, 40)

t.right(110)
t.penup()
t.fd(20)
t.pendown()
t.pensize(10)
t.forward(50)
t.circle(100, 80)
t.pensize(9)
t.circle(150, 50)
t.pensize(7)
t.circle(100, 60)
t.pensize(5)
t.circle(90, 60)
t.pensize(4)
t.circle(40, 60)
t.circle(10, 90)

# head
t.color("red")
t.penup()

t.goto(0, 0)  # Fixed the goto function here

t.goto(-90, 290)  # Fixed the goto function here
t.right(230)
t.pendown()

t.circle(-100, 50)
t.circle(200, 20)
t.circle(50, 30)

t.right(180)

t.circle(50, 30)
t.circle(200, 20)
t.circle(-100, 40)
t.right(95)
t.penup()
t.fd(40)
t.right(90)
t.pendown()
t.circle(100, 40)
t.penup()
t.circle(35, 120)
t.right(30)
t.pendown()
t.pensize(1)
t.circle(60, 50)

# done
t.penup()

t.goto(-70, 90)  # Fixed the goto function here

t.fillcolor("red")
t.begin_fill()
t.circle(20, 180)
t.end_fill()

t.penup()
t.left(75)
t.fillcolor("red")
t.begin_fill()
t.circle(70, 35)
t.end_fill()

t.left(180)
t.backward(10)
t.pendown()
t.left(6)
t.pensize(5)
t.color("red")
t.circle(-80, 40)
t.penup()

t.goto(0, 0)  # Fixed the goto function here

# border
t.write("     Happy Ganesh Chaturthi", font=("arial", 20, "normal"), align="left")

t.color("orange")
t.goto(-240, 420)  # Fixed the goto function here
t.right(90)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.forward(275)
t.right(130)
t.forward(100)
t.end_fill()

t.penup()
t.goto(0, 420)  # Fixed the goto function here
t.right(90)

t.color("orange")
t.fillcolor("orange")
t.begin_fill()
t.fd(100)
t.right(50)
t.pendown()
t.fd(510)
t.left(90)
t.right(165)
t.end_fill()

t.color("orange")
t.fillcolor("orange")
t.begin_fill()
t.fd(540)
t.right(70)
t.fd(20)
t.end_fill()

t.color("orange")
t.fillcolor("orange")
t.begin_fill()
t.fd(540)
t.right(90)
t.fd(20)
t.end_fill()

t.left(30)
t.color("orange")
t.fillcolor("")
t.begin_fill()
t.fd(205)
t.right(90)
t.fd(20)
t.end_fill()

t.color("red")
t.penup()
t.goto(0, 0)  # Fixed the goto function here
t.left(118)
t.fd(240)
t.right(30)
t.pendown()
t.circle(90, 65)
t.penup()

tur.done()
