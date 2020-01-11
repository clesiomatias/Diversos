def media(*valor):
    def soma (valor):
        soma=0
        for i in valor:
            soma +=i
        return soma
    somado = soma(valor)
    media = somado/len(valor)
    return media 
            
    
