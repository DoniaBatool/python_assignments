from turtle import Turtle,Screen

tom=Turtle()
s1=Screen()
s1.bgcolor("black")
tom.color("red","yellow")
tom.penup()
tom.backward(150)
tom.pendown()
tom.speed("fast")
tom.begin_fill()
while True:
    tom.forward(300)
    tom.left(170)
    if tom.heading()==0:
        break
tom.end_fill()

s1.exitonclick()