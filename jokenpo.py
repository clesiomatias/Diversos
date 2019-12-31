import random
for o in range(1,4):
    pc = random.randint(0, 30)
    j = int(input('Para jogar JOKENPO escolha:'
                  '\n1 para pedra'
                  '\n2 para tesoura'
                  '\n3 para papel\n_'
                  ''))

    if pc <= 10:
        pc = 1  # pedra
    elif pc <= 20:
        pc = 2  # papel
    else:
        pc = 3  # tesoura
    if j == 1:
        c = 'Pedra'
    elif j == 2:
        c = 'Tesoura'
    else:
        c = 'Papel'
    if pc == 1:
        d = 'Pedra'
    elif pc == 2:
        d = 'Papel'
    else:
        d = 'Tesoura'
    print('Você escolheu {},  a máquina escolheu {}.'.format(c, d))

    if j == 1:
        if pc == 1:
            print('Empate!')
        elif pc == 2:
            print('Perdeu!')
        else:
            print('Você Venceu!')
    elif j == 2:
        if pc == 1:
            print('Perdeu!')
        elif pc == 2:
            print('Você Venceu!')
        else:
            print('Empate!')
    else:
        if pc == 1:
            print('Você Venceu!')
        elif pc == 2:
            print('Empate!')
        else:
            print('Perdeu!')
