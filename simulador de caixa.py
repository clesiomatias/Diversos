
valor= 0
nota5 = 0
nota10 = 0 
nota20 = 0
nota50 = 0
nota100 = 0
notas = [5,10,20,50,100] 







while True:
	
	operação = int(input('1- Recarregar caixa\n2- Sacar Dinheiro\n3- Sair\nDigite uma opção :'))
	
	if operação == 1:
		for i in notas:
			carga = int(input(f'Digite quantas notas de {i} para inserir:'))
			if i ==5:
				nota5 = carga
				valor+=carga*5
			elif i ==10:
				nota10 = carga
				valor+=carga*10
			elif i ==20:
				nota20 = carga
				valor+=carga*20
			elif i ==50:
				nota50 = carga
				valor+=carga*50
			else:
				nota100 = carga
				valor+=carga*100
		print ( f'''
		valor total em caixa de : {valor}
		temos um total de {nota5} notas de 5 reais
		temos um total de {nota10} notas de 10 reais
		temos um total de {nota20} notas de 20 reais
		temos um total de {nota50} notas de 50 reais
		temos um total de {nota100} notas de 100 reais''')
	elif operação ==2:
		saque = int(input('Digite um valor a sacar: '))
		
		#testando se o valor a ser sacado é divisivel por 5 
		#e se não e maior que o valortotal em caixa
		if saque%5 !=0 or saque>valor:
			print('Valor impossível de ser sacado\nTente novamente!')
		else:
			s = saque
			#retirando do valor total em caixa
			valor-=saque
			de100=0
			de50=0
			de20=0
			de10=0
			de5 =0
			while saque>0:
				
				if saque>=100 and  nota100>0:
					saque-=100
					nota100-=1
					de100+=1
					while saque>=100 and nota100>0:
						saque-=100
						nota100-=1
						de100+=1
						
						
				
				elif saque>=50 and nota50>0:
					saque-=50
					nota50-=1
					de50+=1
					while saque>=50 and nota50>0:
						saque-=50
						nota50-=1
						de50+=1
				
				elif saque>=20 and nota20>0:
					saque-=20
					nota20-=1
					de20+=1
					while saque>=20 and nota20>0:
						saque-=20
						nota20-=1
						de20+=1

				elif saque>=10 and nota10>0:
					saque-=10
					nota10-=1
					de10+=1
					while saque>=10 and nota10>0:
						saque-=10
						nota10-=1
						de10+=1
				
				elif saque>=5 and nota5>0:
					saque-=5
					nota20-=1
					de5+=1
					while saque>=5 and nota5>0:
						saque-=5
						nota20-=1
						de5+=1
				else:
					print('NÃO HÁ NOTAS SUFICIENTES PARA O SAQUE!')
					#repondo o valor do saque no total
					valor+=s
					break
					
			print(f'''Foram entregues:
			{de5} notas de 5
			{de10} notas de 10
			{de20} notas de 20
			{de50} notas de 50
			{de100} notas de 100 
			
			Valor ainda em caixa: {valor}''')
        

			
			
			
		
       
     
    
    
    

		
   
	elif operação ==3:
		break
	else:
		print('Operação inválida!\nTente novamente!')
		print('')
		continue
