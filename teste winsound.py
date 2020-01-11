import turtle
import winsound

def pular():
	winsound.PlaySound('wing.wav',winsound.SND_ASYNC+winsound.SND_PURGE)
	bola.sety(bola.ycor()+30)
    



janela = turtle.Screen()

bola = turtle.Turtle()
bola.speed(0)
bola.pu()
bola.shape('circle')
turtle.listen()
turtle.onkey(pular,'space')


while True:
    bola.sety(bola.ycor()-1)






janela.mainloop()
