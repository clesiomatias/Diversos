import turtle 
def draw_sierpinski(length,depth):
	if depth==0:
		for i in range(0,3):
			turtle.fd(length)
			turtle.left(120)
			turtle.speed(0)
			turtle.ht()
	else:
		draw_sierpinski(length/2,depth-1)
		turtle.fd(length/2)
		draw_sierpinski(length/2,depth-1)
		turtle.bk(length/2)
		turtle.left(60)
		turtle.fd(length/2)
		turtle.right(60)
		draw_sierpinski(length/2,depth-1)
		turtle.left(60)
		turtle.bk(length/2)
		turtle.right(60)
window = turtle.Screen()
draw_sierpinski(800,6)
window.exitonclick()
   
