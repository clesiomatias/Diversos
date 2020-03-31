from turtle import *

setup(500,500)
t1 = Turtle()
t1.shape('turtle')

t1.pensize()
t1.speed(5)
i=0
while t1.xcor()<500 or t1.ycor()<500:
    t1.forward(i*2)
    t1.right(90)
    i+=1
  
