from turtle import Turtle
import turtle                 #1. import modules
from random import randrange

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.down()
leonardo.down()
michelangelo_race = randrange(1, 101)
leonardo_race = randrange(1, 101)
michelangelo.forward(michelangelo_race)
leonardo.forward(leonardo_race)
michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.down()
leonardo.down()
for i in range(0, 10):
  michelangelo_forward = randrange(0, 11)
  leonardo_forward = randrange(0, 11)
  michelangelo.forward(michelangelo_forward)
  leonardo.forward(leonardo_forward)
michelangelo.up()
leonardo.up()
leonardo.goto(-100,-20)
michelangelo.goto(-100, 20)
# Part B - complete part B here
def drawing(first_side, max_side):
  michelangelo = turtle.Turtle()
  michelangelo.color('orange')
  michelangelo.shape('turtle')
  for k in range(first_side, max_side):
    michelangelo.forward(25)
    michelangelo.left(360/(max_side-1))
  michelangelo.clear()
drawing(1, 4)
drawing(1, 5)
drawing(1,7)
drawing(1,10)
drawing(1, 13)

window.exitonclick()
