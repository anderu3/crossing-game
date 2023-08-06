from turtle import Screen
from trucks import Truck
from player import Player
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

inna = Player()

random_truck = Truck()

screen.listen()
screen.onkey(inna.moveup, "Up")
screen.onkey(inna.movedown, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    random_truck.backward(10)



    
screen.exitonclick()
