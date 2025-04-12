import random
import turtle
from turtle import Turtle, Screen
tom = Turtle()
s1=Screen()
print(s1.screensize())
s1.screensize(500,500)
turtle.colormode(255)
tom.penup()
tom.speed(10)
color_list=[(123, 45, 200), (34, 89, 255), (190, 76, 12), (240, 100, 80), (67, 123, 250), 
 (255, 200, 100), (10, 180, 210), (255, 50, 60), (25, 25, 25), (90, 140, 70)]
for _ in range(300):
    tom.pencolor(random.choice(color_list))
    tom.goto(random.randint(-300,300),random.randint(-300,300))
    tom.dot(20)
s1.exitonclick()