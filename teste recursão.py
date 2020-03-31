def imprime_num(x,y):
    if x <= y:
        print(x,end=',')
        x+=1
        return soma(x,y)

def soma(n):
    c=n
    if n >0:
        c += soma(n-1)
    return c
