import random
from turtle import Turtle, Screen
color_list=["Crimson", "Turquoise", "Olive", "Coral", "Indigo", 
          "Sienna", "Teal", "Lavender", "Goldenrod", "Slate Blue"]
WIDTH,HEIGHT=400,400

def no_of_turtle():
    count=0
    while True:
        count=(input("How many Turtles you want to participate in the race (2-10): "))
        if count.isdigit():
            count= int(count)
        else:
            print("Please enter a numeric value between 2 to 10." )
            continue
        if 2<=count<=10:
            return count
        else:
            print("Input is not in the given range....Try again!!")
turtles=no_of_turtle()
print(turtles)
s1= Screen()
s1.setup(400,400)
x_spacing= WIDTH//(turtles+1)
turtle_list=[]

for i in range(1,turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2+(i*x_spacing),-HEIGHT//2+10)
    turtle_list.append(new_turtle)

def race():
    is_race_on= True
    while is_race_on:
        for t in turtle_list:
            distance= random.randrange(1,20)
            t.forward(distance)

            x,y = t.pos()

            if y>=HEIGHT//2-20:
                print(f"Winner is {t.pencolor()} turtle")
                is_race_on = False
race()
s1.exitonclick()