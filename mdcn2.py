def mdcN(*x):
    '''Função codificada em Python que devolve o MDC de 'n' números passados
usando a fórmula:  MDCn = MDC[MDC(n-1), xn] '''
     #recebendo os dois primeiros numeos passados
    x1 = x[0] 
    x2 = x[1]
     #verificando qual dos dois é maior
    if x1>x2:
        maior = x1
        menor = x2
    else:
        maior = x2
        menor = x1
      #calculando o mdc com o Teorema de Euclides (divisões sucessivas)
    while True:
        r = maior%menor
        if r ==0:
            break
        else:
            maior = menor
            menor = r
    #salvando resultado do calculo
    mdc = menor

    #verificando se foram passados mais de dois numeros    
    if len(x)>2:
        #repetindo o calculo até chegar o fim dos numeros passados
        for i in range(2,len(x)):
            x1 = menor
            x2 = x[i]
            if x1>x2:
                maior = x1
                menor = x2
            else:
                maior = x2
                menor = x1
            while True:
                r = maior%menor
                if r ==0:
                    break
                else:
                    maior = menor
                    menor = r
            mdc = menor
     #retornando o resultado final   
    return mdc

       
                
    
    
