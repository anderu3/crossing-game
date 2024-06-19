import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Truck Game")

# Player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.setheading(90)
player.goto(0, -250)

# Truck class
class Truck(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=2)
        self.color(random.choice(["yellow", "green", "red", "blue", "purple", "grey", "black"]))
        self.penup()
        self.goto(350, random.randint(-220, 220))
        self.speed = random.uniform(2, 4) * (1 + level * 0.1) 

    def move(self):
        self.backward(self.speed)

# Function to move the player up
def move_up():
    player.sety(player.ycor() + 20)

# Function to move the player down
def move_down():
    player.sety(player.ycor() - 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# Game variables
trucks = []
level = 1

level_turtle = turtle.Turtle()
level_turtle.hideturtle()
level_turtle.penup()
level_turtle.goto(-290, 260)

# Function to spawn a truck
def spawn_truck():
    new_truck = Truck()
    trucks.append(new_truck)
    screen.ontimer(spawn_truck, random.randint(1000, 3000) // level)

# Function to check for collisions
def check_collision():
    for truck in trucks:
        if player.distance(truck) < 20:
            return True
    return False

def display_level():
    level_turtle.clear()
    level_turtle.write(f"Current Level: {level}", align="left", font=("Arial", 16, "normal"))


# Game loop
display_level()
game_is_on = True
spawn_truck()

while game_is_on:
    time.sleep(0.05)
    screen.update()

    for truck in trucks:
        truck.move()

    if player.ycor() >= 280:
        level += 1
        player.goto(0, -250)
        screen.update()
        display_level()

        if level > 10:
            game_is_on = False

    if check_collision():
        print("Game Over! You collided with a truck.")
        game_is_on = False

screen.bye()
