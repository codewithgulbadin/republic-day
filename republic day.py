import turtle
from turtle import *
import time

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("black")

turtle.speed(1)
turtle.color("white")
# turtle.pendown()
penup()
goto(-50, 70)
turtle.write(
    "codewithgulbadin", #write your name here
    move=False,
    font=("Comic Sans", 24, "bold"))
goto(-100, 20)
turtle.write(
    "codewithgulbadin", #write your name here
    move=False,
    font=("Comic Sans", 24, "bold"))
goto(-30, -25)
turtle.write(
    "codewithgulbadin", #write your name here
    move=False,
    font=("Comic Sans", 24, "bold"))
for i in range(1, 36500):
    bg = turtle.Screen()
    bg.bgcolor("red")
    bg.bgcolor("green")
    bg.bgcolor("cyan")
    bg.bgcolor("blue")
    bg.bgcolor("yellow")
    bg.bgcolor("orange")
    bg.bgcolor("pink")
    bg.bgcolor("green")
    bg.bgcolor("black")
turtle.done()
