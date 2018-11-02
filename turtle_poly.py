# -*- coding: utf-8 -*-
import turtle
#from turtle import Turtle, Screen
#screen = Screen()
#turtle = Turtle(visible=False)

turtle.mode('logo')
#turtle.pensize(3)
#turtle.pencolor('red')
turtle.hideturtle() #不显示箭头

def build_poly():
    turtle.begin_poly()
    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)
    turtle.end_poly()

def build_poly2():
    turtle.begin_poly()
    turtle.right(90)
    turtle.forward(200)
    turtle.end_poly()

build_poly2()

p = turtle.get_poly()
turtle.register_shape("pic", p)
pen = turtle.Turtle()
pen.shape("pic")
pen.penup()
pen.goto(0, 20)
pen2 = turtle.Turtle()
pen2.shape("pic")
pen2.penup()
pen2.goto(0, 40)
turtle.mainloop()
