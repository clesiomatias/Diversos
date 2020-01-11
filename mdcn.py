

'''Função codificada em Python que devolve o MDC de 'n' números passados
usando a fórmula:  MDCn = MDC[MDC(n-1), xn] '''

def mdcN(*x):
    
    '''função interna que tira o mdc de dois numeros por divisões sucessivas'''
    def mdc(x1,x2):
        #definindo maior valor
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
        return menor

    p = mdc(x[0],x[1])
    for i in range(2,len(x)):
        p= mdc(p,x[i])

    return p

       
                
    
    
