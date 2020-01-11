#esse é o dicionario que guarda as perguntas
perguntas = {1:'Qual e o Nome do seu amor?',2:'Qual foi a sua maior loucura de amor?',3:'Se eu Ti Pedisse em Namoro Qual Seria A resposta?',
             4:'Qual e o desporto que Gostas?',5:'Com Que idade início a sua vida Sexual?'}

# Take input from the user// essa primeira pergunta tem de ser feita antes do while
choice = int(input('Escolhe um Numero de 1/91 e eu Respondo a Pergunta\n Depois eu Escolho Tambem Um Numero e tu respondes\n ou digite 0 para sair'))

#esse laço vai repetir até vc escolher 0 como resposta
while choice!=0:
    print('')
    print(perguntas[choice])#aqui vc manda printar a pergunta com o numero escolhido na choice
    '''
    aqui deveria ter um espaço pra resposta, mas no que vc mandou la no grupo nao tem esse espaço
     então da pra continuar, mas vai printar a pergunta escolhida e na sequencia mandar escolher outra pergunta
     mas no geral acho que dá pra entender como funciona, se vc escolher 0 o programa para
     '''
    print('')
    choice = int(input('Escolhe um Numero de 1/91 e eu Respondo a Pergunta\n Depois eu Escolho Tambem Um Numero e tu respondes\n ou digite 0 para sair'))
