import turtle as tt
import random
from time import sleep



#Escopo de funções
def sorteiaCor():
	#lista de caracteres que podem formar uma cor
	lista ='abcdef0123456789'
	cor = '#'
	for i in range(6):
		cor += random.choice(lista)

	return cor

class Quadro(tt.Turtle):
	def __init__(self,x, cor,analisa):
		super().__init__()
		self.ht()
		self.pu()
		self.speed(0)
		self.shape('square')
		self.shapesize(2,3)
		self.color(cor)
		self.setpos(x,-120)
		self.onclick(analisa)
		self.st()
	def cor(self):
		return self.color()
def analisa(x,y):
	print(cor())
			
	
#escopo global
corEscolhida = sorteiaCor()	
	
#Criando janela
janela = tt.Screen()
janela.setup(500,500)
janela.title('Acerte a cor')
janela.bgcolor('black')

#Criando o circulo 
roda = tt.Turtle()
roda.ht()
roda.speed(0)
roda.pu()
roda.setpos(0,100)
roda.shape('circle')
roda.shapesize(12)
roda.pencolor('white')
roda.fillcolor(corEscolhida)
roda.width(10)
roda.st()

# criando os quadros de escolha
x = -200 #coordenada no eixo x para o primeiro quadro
confere = False # variavel que controla as cores
cores = []# lista de cores dos quadros
#-- preenchendo a lista de cores
for i in range(6):
	if not confere and i <5: # confere se ainda não coincidiu com a cor do circulo
		corQuadro = sorteiaCor()
		if corQuadro == corEscolhida:
			confere = True
	elif not confere and i ==5:#se até o final não tiver encontrado a cor é inserida no fim
		corQuadro = corEscolhida
	else: #preenchendo as outros 5 posições
		while True:
			corQuadro = sorteiaCor()
			if corQuadro == corEscolhida:
				continue
			else:
				break
	cores.append(corQuadro) #inserindo a cor na lista
	
quadros=[]
for i in range(6):#criando os quadros
	cor_do_quadro	 = random.choice(cores)
	cores.remove(cor_do_quadro)
	quadros.append(Quadro(x,cor_do_quadro,analisa))
	x+=75



janela.mainloop()
