import turtle

turtle.ht()
turtle.shape('square')
turtle.pu()
turtle.speed(0)
turtle.shapesize(0.2,0.2,0.2)

tese = ['xxxxx xxxxx',
        'xxxx   xxxx',
        'xxx     xxx',
        'xx       xx',
        'x         x',
        'xxxxxxxxxxx']

x=0
y=0

for i in range(len(tese)):
	for n in tese[i]:
		if n in 'x':
			x+=5
		else:
			turtle.stamp()
			x+=5
		turtle.setpos(x,y)
	y-=5
	x=0
