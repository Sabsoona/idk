from logging.handlers import RotatingFileHandler
from tkinter import RIGHT
from tracemalloc import stop
from turtle import *
speed(10)
color("red")
width(1)

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
end_fill()
left(180)

forward(200)


begin_fill()
color("blue")
right(30)
forward(200)
right(120)
forward(200)
end_fill()

left(-120)
forward(180)
color("white")
begin_fill()
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
end_fill()
color("red")
forward(20)
left(90)
forward(200)
left(90)
forward(75)
color("brown")
begin_fill()
left(90)
forward(75)
left(-90)
forward(50)
right(90)
forward(75)
right(90)
forward(50)
end_fill()



exitonclick()
