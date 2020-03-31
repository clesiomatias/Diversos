def tabuada(n):
    
    def imprime(n):
        print(f'Tabuada para o numero {n}')
        for i in range(1,10):
            print(f'{i} x {n} = {i*n}')
    for i in range (1,n+1):
        imprime(i)
    


pp = (lambda x: print(x))
