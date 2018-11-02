# -*- coding: utf-8 -*-
import turtle

turtle.mode('logo')
turtle.hideturtle()

def build_poly():
    turtle.begin_poly()
    turtle.right(90)
    turtle.forward(200)
    turtle.end_poly()

build_poly()

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
