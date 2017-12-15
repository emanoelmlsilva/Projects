import time
from GUI import *

def limparTela():
	print("\n"*50)

def salto(linha,posicaoLinha,direcao,tabuleiro,peça):
	linha = int(linha)
	posicaoLinha = int(posicaoLinha)
	proximalinha = linha
	proximaposicaoLinha = posicaoLinha
	if direcao == "dr" or direcao == "dl":
		proximalinha += 1
		if direcao == "dr":
			if (linha >= 1 and linha <= 4 and proximalinha >= 1 and proximalinha <= 4 or
				linha >= 9 and linha <= 13 and proximalinha >= 9 and proximalinha <= 13):
				proximaposicaoLinha += 1
			elif linha >= 3 and linha <= 4 and proximalinha >= 5 and proximalinha <= 6:
				proximaposicaoLinha += 4
				if linha == 4 and proximalinha == 5:
					proximaposicaoLinha += 1
				if linha == 4 and proximalinha == 6:
					proximaposicaoLinha -= 1

	elif direcao == "dl":
			if (linha >= 5 and linha <= 8 and proximalinha >= 5 and proximalinha <= 8 or
				linha >= 14 and linha <= 17 and proximalinha >= 14 and proximalinha <= 17):
				proximaposicaoLinha -= 1
			elif linha >= 3 and proximalinha <= 6:
				proximaposicaoLinha += 4
				if linha == 4 and proximalinha == 6:
					proximaposicaoLinha -= 1
			elif linha >= 12 and proximalinha <= 15:
				proximaposicaoLinha -= 5

	elif direcao == "ur" or direcao == "ul":
		proximalinha -= 1
		if direcao == "ur":
			if linha == 5 and proximalinha == 4: #or linha == 6
				proximaposicaoLinha -= 4
			elif linha == 14 and proximalinha == 13:
				proximaposicaoLinha += 4
			else:
				proximaposicaoLinha += 1

	print("prox %s"%tabuleiro[proximalinha-1][proximaposicaoLinha-1])

	if tabuleiro[proximalinha-1][proximaposicaoLinha-1] == peça and tabuleiro[linha-1][posicaoLinha-1] == peça:
		print("Salto")
		return True
	else:
		return False

def pegaProximaPosicao(linhaAtual,posicaoLinhaAtual,direcao,salto,tabuleiro,peça,nome):
	if salto == True:
		quantidadeDeLinhasPraPular = 2
	else:
		quantidadeDeLinhasPraPular = 1

	proximaLinha = linhaAtual
	if direcao == "dr" or direcao == "dl":
		proximaLinha += quantidadeDeLinhasPraPular#1
	elif direcao == "ur" or direcao == "ul":
		proximaLinha -= quantidadeDeLinhasPraPular#1

	#Deslocamento
	deslocamento = 0
	if ((linhaAtual >= 1 and linhaAtual <= 4) and (proximaLinha >= 5 and proximaLinha <= 8) or
	 	(linhaAtual >= 14 and linhaAtual <= 17) and (proximaLinha >= 9 and proximaLinha <= 13)):
		deslocamento = 4
	elif ((linhaAtual >= 5 and linhaAtual <= 8) and (proximaLinha >= 1 and proximaLinha <= 4) or
			(linhaAtual >= 9 and linhaAtual <= 13) and (proximaLinha >= 14 and proximaLinha <= 17)):
		deslocamento = -4

	#proximaLinha
	posicaoNaProximaLinha = posicaoLinhaAtual
	if direcao == "ul":
		if ((linhaAtual >= 1 and linhaAtual <= 4) and (proximaLinha >= 1 and proxima <= 4)
			or (linhaAtual >= 9 and linhaAtual <= 13) and (proximaLinha >= 9 and proximaLinha <= 13)
			or (linhaAtual >= 5 and linhaAtual <= 6) and (proximaLinha >= 3 and proximaLinha <= 4)):
			posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular
			if (linhaAtual == 6 and proximaLinha == 4):
				posicaoNaProximaLinha += 1
		else:
			if (linhaAtual <= 11 and proximaLinha >= 8 and linhaAtual != 9):
				posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
			posicaoNaProximaLinha += deslocamento
			if (linhaAtual == 14 and proximaLinha == 12):
				posicaoNaProximaLinha -= 1
	elif direcao == "ur":
		if ((linhaAtual >= 5 and linhaAtual <= 8) and (proximaLinha >= 5 and proximaLinha <= 8) or
			(linhaAtual >= 14 and linhaAtual <= 17) and (proximaLinha >= 14 and proximaLinha <= 17) or
			(linhaAtual >= 14 and linhaAtual <= 15) and (proximaLinha >= 12 and proximaLinha <= 13)):
			posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular
			if linhaAtual == 14 and proximaLinha == 12:
				posicaoNaProximaLinha -= 1
		else:
			posicaoNaProximaLinha += deslocamento
			if (linhaAtual == 9 and proximaLinha == 8) or linhaAtual == 6 and proximaLinha == 4:
				posicaoNaProximaLinha += 1

	elif direcao == "dl":
		if ((linhaAtual >= 5 and linhaAtual <= 8) and (proximaLinha >= 5 and proximaLinha <= 8) or
			(linhaAtual >= 14 and linhaAtual <= 17) and (proximaLinha >= 14 and proximaLinha <= 17) or
			(linhaAtual >= 12 and linhaAtual <= 13) and (proximaLinha >= 14 and proximaLinha <= 15)):
			posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular
			if (linhaAtual == 12 and proximaLinha == 14):
				posicaoNaProximaLinha += 1
		else:
			posicaoNaProximaLinha += deslocamento
			if (linhaAtual == 4 and proximaLinha == 6):
				posicaoNaProximaLinha -= 1
	elif direcao == "dr":
		if ((linhaAtual >= 1 and linhaAtual <= 4) and (proximaLinha >= 1 and proximaLinha <= 4)
			or (linhaAtual >= 9 and linhaAtual <= 13) and (proximaLinha >= 9 and proximaLinha <= 13)
			or (linhaAtual >= 12 and proximaLinha <= 13) and (proximaLinha >= 14 and proximaLinha <= 15)):
			posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular
			if (linhaAtual == 4 and proximaLinha == 6) or (linhaAtual == 12 and proximaLinha == 14):
				posicaoNaProximaLinha -= 1
			elif (linhaAtual == 13 and (proximaLinha >= 14 and proximaLinha <= 15)):
				posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
		else:
			posicaoNaProximaLinha += deslocamento #+ quantidadeDeLinhasPraPular
			if linhaAtual >= 3 and proximaLinha <= 5:
				posicaoNaProximaLinha += quantidadeDeLinhasPraPular
			elif linhaAtual == 4 and proximaLinha == 6:
				posicaoNaProximaLinha += 1

	elif direcao == "l":
		posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
	else:
		posicaoNaProximaLinha += quantidadeDeLinhasPraPular

	if tabuleiro[linhaAtual-1][posicaoLinhaAtual-1] == peça: # and tabuleiro[proximaLinha-1][posicaoNaProximaLinha-1] == "O":
		tabuleiro[linhaAtual-1][posicaoLinhaAtual-1] = "O"
		tabuleiro[proximaLinha-1][posicaoNaProximaLinha-1] = peça
		return tabuleiro
	else:
		Erro("Não é sua peça")
		return movimentacao(tabuleiro,peça,nome)



def separaMovimento(movimento,tabuleiro,peça,nome):
	parada = 0
	linha = ""
	posicaoLinha = ""
	direcao = ""
	for indece in range(len(movimento[0])):
		if movimento[0][indece] == "-" and indece <= 2:
			linha = movimento[0][:indece]
			parada = indece+1
		elif movimento[0][indece] == "-" and indece <= 5:
			posicaoLinha = movimento[0][parada:indece]
			parada = indece+1
		else:
			direcao = movimento[0][parada:]
			dirMovimento = separarDirecao(direcao)

	if len(linha) > 0 and len(linha) <= 2 and len(posicaoLinha) > 0 and len(posicaoLinha) <= 2:
		return linha, posicaoLinha, dirMovimento
	else:
		return movimentacao(tabuleiro,peça,nome)

def verificarMovimento(tabuleiro,linha,posicaoLinha,direcao,peça,nome,movimento):
	if verificarPosicaoAspas(movimento) == True:
		if verificarCondicao(linha,posicaoLinha,direcao) == True:
			if verificarPosicaoLinha(tabuleiro,linha,posicaoLinha) == True:
				if verificarDirecao(direcao) == False:
					Erro("Na direção")
					return movimentacao(tabuleiro,peça,nome)
				else:
					return True
			else:
				Erro("Posição inválida")
				return movimentacao(tabuleiro,peça,nome)
		else:
			Erro("Condição inválida")
			return movimentacao(tabuleiro,peça,nome)
	else:
		Erro("Posição das Aspas")
		return movimentacao(tabuleiro,peça,nome)

def Erro(String):
	limparTela()
	print(" "*50,"Erro, {}".format(String))
	print("\n"*20)
	time.sleep(2)

def verificarPosicaoAspas(movimento):
	quantAspas = 0
	for cont in movimento:
		for indice in range(len(movimento[0])-1,0,-1):
			if movimento[0][indice] == "-":
				quantAspas += 1
				if movimento[0][indice-1] == movimento[0][indice]:
					return False
	if quantAspas < 2:
		return False
	return True

def verificarCondicao(linha,posicaoLinha,direcao):
	dire = "".join(direcao)
	if not linha.isdigit() or not posicaoLinha.isdigit() or not dire.isalpha() or int(linha) < 1 or int(linha) > 17:
		return False
	else:
		return True

def verificarPosicaoLinha(tabuleiro,linha,posicaoLinha):
	if int(posicaoLinha) < 0 or int(posicaoLinha) > len(tabuleiro[int(linha)-1]):
		return False
	else:
		return True

def verificarDirecao(direcao):
	for separar in direcao:
		if separar != "l" and separar != "r" and separar != "dl" and separar != "dr" and separar != "ul" and separar != "ur":
			return False

def separarDirecao(direcao):
	direcAnterior = 0
	dirMovimento = []
	for direc in range(len(direcao)):
		if direcao[direc] == "-":
			if len(direcao[direcAnterior:direc]) == 1:
				dirMovimento.append(direcao[direcAnterior:direc])
			else:
				dirMovimento.append(direcao[direcAnterior:direcAnterior+2])
			direcAnterior = +direc+1
	dirMovimento.append(direcao[direcAnterior:])
	return dirMovimento

def criarTabuleiro():
    tabuleiro = []

    for linha in range(4):
        tabuleiro.append([])
        for coluna in range(linha+1):
            tabuleiro[linha].append("O")

    posi = 13
    for linha in range(4,8):
        tabuleiro.append([])
        for coluna in range(posi):
            tabuleiro[linha].append("O")
        posi -= 1

    for linha in range(8,13):
        tabuleiro.append([])
        for coluna in range(linha+1):
            tabuleiro[linha].append("O")

    posi = 4
    for linha in range(13,17):
        tabuleiro.append([])
        for coluna in range(posi):
            tabuleiro[linha].append("O")
        posi -= 1

    return tabuleiro

def adicionarPecas(tabuleiro,quantJogador,peça):
	if quantJogador == 2:
		PrimeiraParteTabuleiro(tabuleiro,peça[0])
		UltimaParteTabuleiro(tabuleiro,peça[1])

	elif quantJogador == 3:
		UltimaParteTabuleiro(tabuleiro,peça[0])
		SegundaParteTabuleiro(tabuleiro,peça[1],peça[2])

	elif quantJogador == 4:
		SegundaParteTabuleiro(tabuleiro,peça[0],peça[1])
		TerceiraParteTabuleiro(tabuleiro,peça[2],peça[3])

	elif quantJogador == 6:
		SegundaParteTabuleiro(tabuleiro,peça[1],peça[2])
		TerceiraParteTabuleiro(tabuleiro,peça[3],peça[4])
		PrimeiraParteTabuleiro(tabuleiro,peça[0])
		UltimaParteTabuleiro(tabuleiro,peça[5])

	return tabuleiro

def PrimeiraParteTabuleiro(tabuleiro,peça):
	for numLinha,linha in enumerate (tabuleiro[:4]):
		for numColuna,coluna in enumerate (linha):
			tabuleiro[numLinha][numColuna] = peça


def UltimaParteTabuleiro(tabuleiro,peça):
	for numLinha,linha in enumerate(tabuleiro[13:]):
		for numColuna,coluna in enumerate (linha):
			tabuleiro[numLinha+13][numColuna] = peça


def SegundaParteTabuleiro(tabuleiro,peça,peça2):
	quantColuna = 4
	numLinha = 4
	for linha in tabuleiro[4:8]:
		for numColuna in range(quantColuna):
			tabuleiro[numLinha][numColuna] = peça
		quantColuna -= 1
		numLinha += 1

	quantColuna = -4
	numLinha = 4
	for linha in tabuleiro[4:8]:
		for numColuna in range(quantColuna,0):
			tabuleiro[numLinha][numColuna] = peça2
		quantColuna += 1
		numLinha += 1

def TerceiraParteTabuleiro(tabuleiro,peça,peça2):
	quantColuna = 1
	numLinha = 9
	for linha in tabuleiro[9:13]:
		for numColuna in range(quantColuna):
			tabuleiro[numLinha][numColuna] = peça
		quantColuna += 1
		numLinha += 1

	quantColuna = 10
	numLinha = 9
	for linha in tabuleiro[9:13]:
		for numColuna in range(9,quantColuna):
			tabuleiro[numLinha][numColuna] = peça2
		quantColuna += 1
		numLinha += 1
