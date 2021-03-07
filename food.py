from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.spawn()

    def spawn(self):
        x = random.randint(-280, 299)
        y = random.randint(-280, 299)
        x, y = x - (x % 20), y - (y % 20)
        self.goto(x, y)