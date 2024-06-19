from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def moveup(self):
        self.fd(20)

    def movedown(self):
        self.backward(20)
