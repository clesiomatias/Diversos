from turtle import *

janela = Screen()
janela.setup(400,400)
janela.bgcolor('blue')

figura = Turtle()
figura.speed(0)
figura.pu()
figura.color('red')
figura.shape('turtle')
figura.ht()

def estampar(x,y):
	global figura
	figura.setpos(x,y)
	figura.stamp()
	



janela.onclick(estampar)

janela.mainloop()
