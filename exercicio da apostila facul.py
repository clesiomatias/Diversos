maior =0
nnumero = 0
for i in range(10):
    nota = float(input(f'Digite a nota do {i+1}º aluno:'))
    if nota > maior:
        maior = nota
        numero = i+1
print(f'A maior nota foi {maior}, do {numero}º Aluno.')
