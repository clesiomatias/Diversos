import turtle

d = turtle.Turtle()
d.speed(0)
d.pu()
d.color('#ff33ff')
d.shape('square')

def click(x,y):
	print(d.fillcolor())

d.onclick(click)

turtle.mainloop()
