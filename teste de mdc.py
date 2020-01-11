from mdcn2 import *
resp = ''
lista =[]
while True:
    resp = int(input('Digite quantos numeros serão calculados\nOu digite 0 pra sair: '))
    if resp == 0:
        break
    else:
        for i in range(resp):
            num = int(input(f'Digite o {i+1}º número: '))
            lista.append(num)
        print(mdcN(*lista))
    
            
