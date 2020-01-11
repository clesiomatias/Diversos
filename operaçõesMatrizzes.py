def soma_matrizes(*m):
    '''função que recebe 'n' matrizes e retorna sua soma'''
    m1 = m[0]
    m2 = m[1]
    if len(m1)!= len(m2) or len(m1[0]) != len(m2[0]):
        return 0
    else: 
        def soma2matrizes(m1,m2):
            soma = []
            for i in range(len(m1)):
                nova=[]
                for j in range(len(m1[0])):
                    nova.append(m1[i][j]+m2[i][j])
                soma.append(nova)
            return soma
        soma = soma2matrizes(m1,m2)
        for i in range(2,len(m)):
            m1 = soma
            m2 = m[i]
            if len(m1)!= len(m2) or len(m1[0]) != len(m2[0]):
                return 0
            else:
                soma = soma2matrizes(m1,m2)
        return soma
                
        
def multi_matrizes(*m):
    '''Função que recebe 'n' matrizes e retorna o produto delas'''
    m1 = m[0]
    m2 = m[1]
    if len(m1) > len(m2):
        mt=m1
        m1=m2
        m2=mt
    if len(m1[0]) != len(m2) and len(m2[0]) != len(m1):
        return 0
    else:
        def multi2matrizes(m1,m2):
            multi = []

            for i in range(len(m1)):
                nova=[]
                
                for j in range(len(m2[0])):
                    r=0
                    for m in range(len(m1)):
                        r += (m1[i][m]*m2[m][j])
                    nova.append(r)
                multi.append(nova)
            return multi
        multi = multi2matrizes(m1,m2)
    for i in range(2,len(m)):
        m1 =multi
        m2 = m[i]
        if len(m1)<len(m2):
                mt=m1
                m1=m2
                m2=mt
        multi = multi2matrizes(multi,m[i])
    return multi

