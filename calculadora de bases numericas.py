'''
Programa de conversão de bases numéricas
usando interface gráfica do módulo interno Tkinter

@version 1.0
@author Clésio Matias
@email clesiofmatias@gmail.com
'''
#ESCOPO DE FUNÇÕES
#=-=-=-=-=-=-=-=-=-=-=

#converter base 10 para binário
def dez_para_binario(x):
    x = int(x)
    z=1
    l =[]
    while True:
        z*= 2
        if z>=x:
            break
        
    while True:
        if x==0 and z==0.5:
            break
        l.append(int(x//z))
        x=int(x%z)
        z/=2
    if l[0]==0:
        del l[0]
    return l
        
        
#converter base 10 para hexa
def dez_para_hexa(x):
    x=int(x)
    z=1
    l =[]
    while True:
        z*= 16
        if z>=x:
            break
        
    while True:
        if x//z == 10:
            l.append('A')
        elif x//z == 11:
            l.append('B')
        elif x//z == 12:
            l.append('C')
        elif x//z == 13:
            l.append('D')
        elif x//z == 14:
            l.append('E')
        elif x//z == 15:
            l.append('F')
        else:
            l.append(int(x//z))
        x=int(x%z)
        z/=16
        if x<=0 and z<=1:
            break
    if l[0]==0:
        del l[0]
    return l

        
#converter base hexa para binário
def hexa_para_binario(x):
    n = str(x)
    
    l = []
    l2 = []
    l3=[]
    pos=0
    
    while pos < len(n) :
        l.append(n[pos])
        pos+=1
    
    for i in l:
        if i in'012345679':
            i= int(i)
        elif i in 'aA':
            i =10
        elif  i in 'bB':
            i =11
        elif i in 'cC':
            i =12
        elif i in 'dD':
            i =13
        elif i in 'eE':
            i =14
        elif i in 'fF':
            i=15
        c = dez_para_binario(i)
        
        while True:
            if len(c)<4:
                c.insert(0,0)
            else:
                break
        l2.append(c)
    for i in l2:
        for j in i:
            l3.append(j)
    if l3[0]==0:
        del l3[0]
    return l3


#converter binário para base 10
def binario_para_dez(x):
    l=[]
    num=[]
    d =0
    for i in x:
        if i  in '0' or  i in '1':
            l.append(i)
    l.reverse()
    for i in l:
        num.append(int(i))
    for i in range (0,len(num)):
        if num[i]!=0:
            d+=(2**i)
    return d


# INICIO DO CORPO DO PROGRAMA
#*{

    #importando pacote grafico Tkinter
from tkinter import *

j1 = Tk()  #Criando a janela de menus
j1.title('C.bases')
f = Frame(j1)
f.grid()


#funções de controles de botão
def bt_onclick1():
    i=str(lEnt.get())
    e=str(hexa_para_binario(i))
    d= binario_para_dez(e)
    lRes['text'] = str(d)
def bt_onclick2():
    i=str(lEnt.get())
    e=str(hexa_para_binario(i))
    lRes['text'] = str(e)
def bt_onclick3():
    i=str(lEnt.get())
    e=str(binario_para_dez(i))
    lRes['text'] = str(e)
def bt_onclick4():
    i=str(lEnt.get())
    e=str(binario_para_dez(i))
    d=str(dez_para_hexa(e))
    lRes['text'] = str(d)
def bt_onclick5():
    i=str(lEnt.get())
    e=str(dez_para_binario(i))
    lRes['text'] = str(e)
def bt_onclick6():
    i=str(lEnt.get())
    e=str(dez_para_hexa(i))
    lRes['text'] = str(e)

    
#criando botões de menu
b1 = Button(f,text = 'Hexa para Decimal', command = bt_onclick1)
b2 = Button(f,text = 'Hexa para Binário',command = bt_onclick2)
b3 = Button(f,text = 'Binário para Decimal',command = bt_onclick3)
b4 = Button(f,text = 'Binário para Hexa',command = bt_onclick4)
b5 = Button(f,text = 'Decimal para Binário',command = bt_onclick5)
b6 = Button(f,text = 'Decimal para Hexa',command = bt_onclick6)
#conectando botões à janela de menus
b1.grid()
b2.grid()
b3.grid()
b4.grid()
b5.grid()
b6.grid()

#criando labels de entrada de dados e resultados
lEnt = Entry(j1)
lRes = Label(j1, text = '0')
lEnt.grid()
lRes.grid()

j1.mainloop() #loop da janela

# *}
#fim do corpo do programa principal
