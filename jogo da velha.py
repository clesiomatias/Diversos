import turtle
import random
import time

turtle.register_shape('x.gif')
turtle.register_shape('o.gif')
player = True
ganhou = False
jogando = True
decisão = None
posições=[(-200,200),(0,200),(200,200),(-200,0),(0,0),(200,0),(-200,-200),(0,-200),(200,-200)]
quadros =  ['-','-','-','-','-','-','-','-','-']
janela = None

# criar janela
def cria_janela():
	global ganhou, decisão, janela
	janela = turtle.Screen()
	janela.setup(600,600)
	janela.title('Jogo da Velha')
	janela.bgcolor('blue')
	janela.onscreenclick(jogar)
	


	#criando as linhas
	linha = turtle.Turtle()
	linha.ht()
	linha.speed(0)
	linha.color('red')
	linha.width(10)
	linha.pu()
	linha.setpos(-100,-305)
	linha.pd()
	linha.goto(-100,305)
	linha.setpos(100,305)
	linha.goto(100,-305)
	linha.pu()
	linha.setpos(-305,-100)
	linha.pd()
	linha.goto(305,-100)
	linha.setpos(305,100)
	linha.goto(-305,100)
	janela.mainloop()
	
	
	
	

def jogar(x,y):
    global posições, player,quadros,decisão,janela
    colunas = (x+300)//200
    linhas = (-y+300)//200
    quadrados = colunas+linhas*3
    quadrados = int(quadrados)
    try:
        jogada = turtle.Turtle()
        jogada.ht()
        if player:
            player = False
            forma = 'x.gif'
            if quadros[quadrados]== '-':
                quadros[quadrados] = 'x'
        else:
            player = True
            forma = 'o.gif'
            if quadros[quadrados] =='-':
                quadros[quadrados] = 'o'
        jogada.shape(forma)
        jogada.pu()
        jogada.speed(0)
        jogada.setpos(posições[quadrados])
        posições[quadrados]= None
        jogada.st()
        analisar()
        if ganhou:
			janela.clear()
			
        
          
        
    except:
       pass
   

def analisar():
    global quadros,ganhou
    if quadros[0]!='-' and quadros[0] == quadros[1] and quadros[0] == quadros[2] :
        ganhou =True
        print('ganhou')
    elif quadros[1]!='-' and quadros[1] == quadros[4] and quadros[1] == quadros[7]:
        ganhou =True
        print('ganhou')
    elif quadros[2]!='-' and quadros[2] == quadros[5] and quadros[2] == quadros[8]:
        ganhou =True
        print('ganhou')
    elif quadros[3]!='-' and quadros[3] == quadros[4] and quadros[3] == quadros[5]:
        ganhou =True
        print('ganhou')
    elif quadros[6]!='-' and quadros[6] == quadros[7] and quadros[7] == quadros[8]:
        ganhou =True
        print('ganhou')
    elif quadros[0]!='-' and quadros[0] == quadros[3] and quadros[0] == quadros[6]:
        ganhou =True
        print('ganhou')
    elif quadros[0]!='-' and quadros[0] == quadros[4] and quadros[0] == quadros[8]:
        ganhou =True
        print('ganhou')
    elif quadros[2]!='-' and quadros[2] == quadros[4] and quadros[2] == quadros[6] :
        ganhou =True
        print('ganhou')
    print(ganhou)
   
cria_janela()

       
