# -*- coding: utf-8 -*-
#掏出一盒画图笔
import turtle

#从盒中拿出一直铅笔，给它起个名字叫magicPen
magicPen=turtle.Pen()

#请问画个正方形需要几步？
#先画一条长100的直线
magicPen.forward(100)
#笔头转90度
magicPen.left(90)

#重复上面这个步骤三次
magicPen.forward(100)
magicPen.left(90)

magicPen.forward(100)
magicPen.left(90)

magicPen.forward(100)
magicPen.left(90)

#画完了，让我我看下
turtle.mainloop()
#记得把画笔盒子关上
turtle.exitonclick()
turtle.bye()
#turtle.done()
