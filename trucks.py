from turtle import Turtle
import random

list_of_colors = ["yellow", "green", "red", "blue", "purple", "grey", "black"]

class Truck(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=2)
        self.color(list_of_colors[random.randint(0, 6)])
        self.goto(350, (random.randint(-220, 220)))

    def truck_route(self):
        """Moves the truck from right to left until off screen"""
        if self.xcor() < 351 and self.xcor() > -350:
            self.backward(10)

