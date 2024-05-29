from turtle import *


#we want build house

#step1: draw a square
speed(40)
width(7)
color("dark blue") 
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)


#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window

penup()
goto(170, 170)
pendown()


right(160)
color("green")
left(100)
forward(50)
right(-90)
forward(40)
left(90)
forward(50)
right(-90)
forward(40)


penup()
goto(35, 130)
pendown()


right(190)
color("green")
left(100)
forward(50)
right(-90)
forward(40)
left(90)
forward(50)
right(-90)
forward(40)

def draw_stick_figure(x, y):
    penup()
    goto(200,-200)
    pendown()
    circle(10)

    right(90)
    forward(30)
    left(45)
    forward(20)
    backward(20)
    right(90)
    forward(20)
    backward(20)
    left(45)
    forward(20)
    backward(20)
    right(45)
    forward(30)
    backward(30)
    left(90)
    forward(30)    
    backward(30)


width(10)

draw_stick_figure(0, 0)

exitonclick()    

























