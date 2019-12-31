from turtle import *
import time
import random

class Tartaruga(Turtle):
	
	def __init__(self,numero,cor,x,y ):
		super().__init__()
		self.ht() 
		self.speed(0)
		self.pu()
		self.color(cor)
		self.setpos(x,y)
		self.shape('turtle')
		self.shapesize(2)
		self.pd()
		self.st()
		self.numero = numero
		
	def correr(self,x,y):
		self.goto(x,y)
	
janela = Screen()
janela.bgcolor('white')
janela.title('Corrida de Tartaruga')
janela.setup(500,400)

linha= Turtle()
linha.ht()
linha.pu()
linha.speed(0)
linha.setpos(235,195)
linha.color('red')
linha.width(2)
linha.pd()
linha.goto(235,-195)

y = 160
x = -220
cores=['red', 'yellow','blue','gray','purple']
tartarugas =[]
for i in range(5):
	tartarugas.append( Tartaruga(i,cores[i],x,y))
	y-= 75
time.sleep(1)	
while True:
    if tartarugas[0].xcor()>=200 or tartarugas[1].xcor()>=200 or tartarugas[2].xcor()>=200 or tartarugas[3].xcor()>=200 or tartarugas[4].xcor()>=200 :
            break
    else:
			
            for i in range(len(tartarugas)):
					
                    tartarugas[i].correr(tartarugas [i].xcor ()+random.randint (0,5),tartarugas[i].ycor ())
                    print(tartarugas[i].numero,' =' ,tartarugas[i].xcor())
   
janela.mainloop()
	
