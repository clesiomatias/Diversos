from tkinter import *
import time

janela = Tk()
janela.geometry("300x300+200+200")

x = 145
texto = StringVar()

def delay(tempo):
     time.sleep(tempo)

def bt_clk():
     bt1.place(x=100,y=120)
     bt1["width"] = 13
     bt1["text"] = "Aumentar largura"
     bt1["command"] = bt_clk2
     bt2.place(x=100,y=150)
     bt1.place(x=100, y=120)
     bt3.place(x=145, y=180)

def bt_clk2():
     global x
     x -= 3.5
     bt3["width"] += 1
     bt3.place(x=x,y=180)
     if bt3["width"] >= 0:
          texto.set('')

def bt_clk3():
     global x, texto
     x += 3.5
     bt3["width"] -= 1
     bt3.place(x=x, y=180)
     print (bt3["width"],texto)
     
     if bt3["width"] <=1:
          texto.set('Nao da pra diminuir mais!')
          x -= 3.5
          bt3["width"] = 0
          bt3.place(x=x, y=180)
     
bt1 = Button(janela, width=5, height=1, text="Iniciar", command=bt_clk)
bt1.place(x=128, y=135)

bt2 = Button(janela, width=13, height=1, text="Diminuir largura", command=bt_clk3)

bt3 = Button(janela, width=0, height=1)

lb1 = Label(janela, textvariable = texto)
lb1.place(x=80, y=210)
lb1.pack()

janela.mainloop()
