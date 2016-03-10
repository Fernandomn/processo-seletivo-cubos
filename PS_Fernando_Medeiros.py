import math

def somaColunas(coluna, matrizEntrada):
	resultado = 0
	for i in range(len(matrizEntrada)):
		if(i != coluna):
			resultado += matrizEntrada[i][coluna]
	return resultado	

def testeColunas (matrizEntrada):
	for j in range(len(matrizEntrada[0])-1):
		if j < len(matrizEntrada):
			if not (math.fabs(matrizEntrada[j][j]) > math.fabs(somaColunas(j, matrizEntrada))):
				return False
		else: 
			return False		
	return True

def somaLinhas(linha, matrizEntrada):
	resultado = 0
	for j in range(len(matrizEntrada[linha])-1):
		if(j != linha):
			resultado += matrizEntrada[linha][j]
	return resultado		

def testeLinhas (matrizEntrada):
	for i in range(len(matrizEntrada)):
		if i < len(matrizEntrada[i]):
			if not (math.fabs(matrizEntrada[i][i]) > math.fabs(somaLinhas(i, matrizEntrada))):
				return False
		else: 
			return False
	return True

def maiorCoefAbsoluto(linhaMatriz):
	maior = 0
	indice = 0
	for i in range(len(linhaMatriz)):
		soma=0
		for j in range(len(linhaMatriz)):
			if(i!=j):
				soma += linhaMatriz[j]

		if math.fabs(linhaMatriz[i]) > math.fabs(soma) and math.fabs(linhaMatriz[i]) > maior:
			maior = math.fabs(linhaMatriz[i])
			indice = i
	return indice	

def correcaoLinhas(matrizEntrada):
	registroLinhas=[]
	matrizEntradaCorrigida=[]
	for i in range(len(matrizEntrada)):
		linhaAux = matrizEntrada[i][:-1]
		registroLinhas.append((maiorCoefAbsoluto(linhaAux), i))
	registroLinhas.sort()
	for j in registroLinhas:
		matrizEntradaCorrigida.append(matrizEntrada[j[1]])

	return	matrizEntradaCorrigida

def MetodoGauss(matrizEntrada) :	
	qntLinhas = len(matrizEntrada)
	qntColunas = len(matrizEntrada[0])-1

	if not testeLinhas(matrizEntrada) or not testeColunas(matrizEntrada):
		#print("A matriz não obedece aos critérios das linhas/colunas. Não é possivel garantir sua convergência")
		#print("Serão efetuadas mudanças na posição das linhas da matriz, para que se adequem ao critério das linhas")
		matrizEntrada = correcaoLinhas(matrizEntrada)

	#eliminação
	for j in range(qntLinhas-1):		
		itemDiagonalPrincipal = matrizEntrada[j][j]
		if itemDiagonalPrincipal!=0:
			#print("matrizEntrada "+str(matrizEntrada))
			for i in range(j+1, qntLinhas):
				itemLinha = matrizEntrada[i][j]				
				multiplicador = float(itemLinha/itemDiagonalPrincipal)
				for k in range(len(matrizEntrada[i])):
					if((i,k)!=(j,j)):
						matrizEntrada[i][k] = float(matrizEntrada[i][k] - multiplicador*matrizEntrada[j][k])				
		else:
			print("O sistema apresentou o valor nulo na diagonal principal. Ele não tem solução real (impossível ou indeterminado).")
			return []

	#substituição	
	matrizResposta = []
	for numRespostas in range(qntColunas):
		matrizResposta.append(0)
	if(matrizEntrada[qntColunas-1][qntColunas-1] ==0):
		print("O sistema não possui solução real")
		return []
	matrizResposta[-1] = (float(matrizEntrada[qntColunas-1][qntColunas] / matrizEntrada[qntColunas-1][qntColunas-1]))

	for i in range(qntLinhas-2, -1, -1):
		somaRespostas = 0
		for j in range(i,qntLinhas):
			somaRespostas += float(matrizEntrada[i][j] * matrizResposta[j])
		if matrizEntrada[i][i]==0:
			print("O sistema não possui solução real")
			return []	
		matrizResposta[i] = float((matrizEntrada[i][-1] - somaRespostas)/matrizEntrada[i][i])
	return matrizResposta
	
def insereMatriz():
	print("Insira as equações do sistema linear. Coloque os valores dos coeficientes em ordem, ignorando as varáveis, separadas por um espaço. Separe o resultado com um igual")
	print("Exemplo, 5x + 3y - z = 4 seria\n5 3 -1 = 4")
	print("Digite qualquer letra para interromper o cadastro de equações e iniciar a resolução do sistema")
	print("Coeficientes nulos devem ser explicitados. Exemplo:")
	print("5x + 3z = 7 seria\n5 0 3 = 7")
	print("podem ser usados tanto numeros fracionarios, na forma x/y, como em decimal, x.y")
	
	coef = ""
	matrizEntrada = []
	linhaEntrada = []
	resultado = False
	while(not coef.isalpha()):
		linhaEntrada = []
		equacao = input()
		vetorEquacao = equacao.split(' ')
		for coef in vetorEquacao:
			if coef.isalpha():
				break
			if(coef=='='):
				continue
			else:
				linhaEntrada.append(eval(coef))
		if not coef.isalpha():
			matrizEntrada.append(linhaEntrada)	
			
	#print("matrizEntrada "+str(matrizEntrada))		
	tamAnterior = 0		
	for linha in range(len(matrizEntrada)):
		if linha == 0:
			tamAnterior = len(matrizEntrada[linha])
		elif tamAnterior!= len(matrizEntrada[linha]):
			print("A matriz não está no formato errado. A linha " + str(linha) + " tem um tamanho diferente das anteriores. Deseja reiniciar o processo? [s/n]")
			if input().lower() =="s":
				return	insereMatriz()
			else:
				return []	
		elif linha == len(matrizEntrada)-1 and not(len(matrizEntrada) == len(matrizEntrada[linha])-1):
			print("O numero de linhas cadastradas esta diferente do numero de coeficientes. Deseja refazer o processo? [s/n]")
			#print("(Caso deseje cadastradar uma linha nula, coloque 0 como os valores dos coeficientes)")
			if input().lower() =="s":
				return	insereMatriz()

	return matrizEntrada			

def main():
	
	#matrizEntrada = [[4, -1, -1, 1, 1],
	#				[1, -12, 5, -4, 11],
	#				[0, 1, 3, -1, -5],
	#				[-2, 1, -4, 10, 3]]
	#matrizEntrada = [[-2, 1, -4, 10, 3],
	#				[4, -1, -1, 1, 1],
	#				[0, 1, 3, -1, -5],
	#				[1, -12, 5, -4, 11]]

	matrizEntrada = insereMatriz()				
	if len(matrizEntrada) > 0:
		matrizResposta = MetodoGauss(matrizEntrada)
		if len(matrizResposta) > 0:
			print("O resultado do sistema é:")
			for i in range(len(matrizResposta)):
				print("x"+str(i)+ " = " + str(matrizResposta[i]))

	return 0

if __name__ == '__main__':
	main()
