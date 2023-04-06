from turtle import Turtle
from random import randint

class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.pu()
        self.food.hideturtle()
        self.food.dot(10,"blue")
    
    def new_food(self):
        self.xcor_food = randint(-350,350)
        self.ycor_food = randint(-350,350)
        self.food.goto(self.xcor_food,self.ycor_food)


    