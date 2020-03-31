import pygame
from pygame.locals import*
from OpenGL.GL import *

larg_janela = 640
alt_janela = 480

xDaBola =0
yDaBola =0
tamanhoDaBola = 20
vel_da_bolaEmx = 3
vel_da_bolaEmy =3
yDoJog1 = 0
yDoJog2 = 0

pygame.init()
pygame.display.set_mode((larg_janela.alt_janela),DOUBLEBUF|OPENGL)


def atualizar():
    
    pass
  

def desenhar():
    pass

while True:
    atualizar()
    desenhar()
