import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
tom = turtle.Turtle()
tom.speed(10)  # Fastest drawing

colors = ["red", "yellow", "green", "blue", "orange", "purple"]

# Draw polygons centered around the middle
for i in range(3, 9):  # 3 to 8 sides
    angle = 360 / i
    tom.penup()
    tom.home()  # Go to center and reset heading
    tom.forward(50)  # Move forward to avoid overlap
    tom.right(90)  # Rotate to position shape downward a bit
    tom.pendown()
    
    tom.pencolor(random.choice(colors))
    
    for _ in range(i):
        tom.forward(100)
        tom.right(angle)

turtle.done()
