# Escopo de importações
#--- import do modulo gráfico Turtle
import turtle as tt
import random

# import do modulo ctypes, e o usando para "pegar" as dimensões da tela
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def sortCor():
    caracteres = 'abcdef0123456789'
    cor = '#'
    for i in range (6):
        escolha = random.choice(caracteres)
        cor+=escolha
    return cor

escolhido = sortCor()

#-- Criando janela --#

janela = tt.Screen()
janela.bgcolor("#eeffcc")
janela.title('Joguinho')
janela.setup(screensize[0]-20,screensize[1]-80,0,0)

#--criando o circulo central --#

centro = tt.Turtle()
centro.speed(0)
centro.pu()
centro.ht()
centro.shapesize(20,20)
tamanho= centro.shapesize()
centro.setpos(0-tamanho[0],0+tamanho[1]*5)
centro.shape('circle')
centro.color(escolhido)
centro.st()

#-- criando os quadros de adivinhação --#
quadros =[]
for i in range (6):
  quadros.append(tt.Turtle())
x = -450
valor =[0,1,2,3,4,5]
for i in quadros:
    i.speed(0)
    i.pu()
    i.ht()
    i.shape('square')
    i.shapesize(5,5)
    i.setpos(x,-220)
    i.st()
    try:
        certo = random.choice(valor)
    except:
        pass
    if quadros.index(i) == certo:
        i.color(escolhido)
        valor.clear()
    elif quadros.index(i) == 5 and len(valor)>0:
        i.color(escolhido)
    else:
        i.color(sortCor())
    x+= 180

    







