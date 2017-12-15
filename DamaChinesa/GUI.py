import time
import bibliotecaDamaChinesa

def menuInicial(): # GUI
	limparTela()

	print("|"+"="*148+"|")
	print("|"+"="*148+"|")
	print("|"+"="*70+" Tabuleiro "+"="*67+"|")
	print("|"+"="*148+"|")
	print("|"+"="*148+"|")
	print("\n"*4)
	tabuleiro = bibliotecaDamaChinesa.criarTabuleiro()

	imprimirTabuleiro(tabuleiro) # GUI
	print("\n\n")

	quantidadejogador = input(" "*55+"Infome a quantidade de jogadores: ")
	if quantidadejogador.isdigit() == True:
		if int(quantidadejogador) < 2 or int(quantidadejogador) == 5 or int(quantidadejogador) > 6:
			limparTela()
			print("Valor Invalida, Informe um numéro 2 ,3 ,4 ou 6")
			time.sleep(3)
			return menuInicial() #GUI
	else:
		print("Valor Invalida, Não e um numéro")
		time.sleep(3)
		return menuInicial() #GUI

	return int(quantidadejogador)


def limparTela():
	print("\n"*50)

def nomeDosJogadores(quantidadejogador): #ANA
	peça = ["R","N","C","B","A","V"]
	#        0   1   2   3   4   5
	nome = []
	for i in range(quantidadejogador):
		nome.append(input("Informe o nome do jogador {}: ".format(i+1)))

	if quantidadejogador == 2:
		retur = peça[0],peça[5]
	elif quantidadejogador == 3:
		retur = peça[1],peça[2],peça[5]
	elif quantidadejogador == 4:
		retur = peça[1:6]
	elif quantidadejogador == 6:
		retur = peça
	return nome,retur

def mostrarJogador(quantidadejogador,retur):
	limparTela()
	if quantidadejogador == 2:
		print("Jogador 1: {}".format(retur[0]),end=" /")
		print("Jogador 2: {}".format(retur[1]))
		#retur = peça[0],peça[5]
	elif quantidadejogador == 3:
		print("Jogador 1: {}".format(peça[1]),end=' /')
		print("Jogador 2: {}".format(peça[2]),end=' /')
		print("Jogador 3: {}".format(peça[5]))
		#retur = peça[1],peça[2],peça[5]
	elif quantidadejogador == 4:
		for i in range(1,5):
			print("Jogador {}: {}".format(i+1,peça[i]),end=" /")
		print("\n\n")
	#	retur = peça[1:6]
	elif quantidadejogador == 6:
		for i in range(quantidadejogador):
			print("Jogador {}: {}".format(i+1,peça[i]),end=" /")
		print("\n\n")
		#retur = peça
	#return retur

def movimentacao(tabuleiro,nome,peça):
	imprimirTabuleiro(tabuleiro)
	print("|"+"="*40+"|")
	print("{}Vez do Jogador {} / peça {}".format(' '*9,nome,peça)) #erro na quantidade de jogadores
	print("|"+"="*40+"|\n")
	print("_"*107)
	print("/l para left | r para right | ul para up-left | ur para  up-right | dl para down-left | dr para down-right/")
	print("_"*84)
	print("/Para movermos uma peça utilizar o, seguinte padrão: <linha-posiçãoNaLinha-direção>/")
	print("_"*105)
	print("/Ex: para mover com apenas um salto basta colocar 17-1-ur, se for com mais de um salto coloca 17-1-ur-ul/\n")
	movimento=[]
	movimento.append(input("Digite o movimento: "))
	if len(movimento[0]) >= 5:
		linhaAtual,posicaoLinhaAtual,direcao = bibliotecaDamaChinesa.separaMovimento(movimento,tabuleiro,peça,nome)
		bibliotecaDamaChinesa.verificarMovimento(tabuleiro,linhaAtual,posicaoLinhaAtual,direcao,peça,nome,movimento)
		for x in range(len(direcao)):
			salto = bibliotecaDamaChinesa.salto(linhaAtual,posicaoLinhaAtual,direcao[x],tabuleiro,peça)
			tabuleiro = bibliotecaDamaChinesa.pegaProximaPosicao(int(linhaAtual),int(posicaoLinhaAtual),direcao[x],salto,tabuleiro,peça,nome)
		imprimirTabuleiro(tabuleiro)
	else:
		bibliotecaDamaChinesa.Erro("No movimento")
		return movimentacao(tabuleiro,nome,peça)

def imprimirLinhaComEspaco(tabuleiro,linha,espaco):
	print(40*" ",linha+1,espaco*" ",end="")
	for i in tabuleiro[linha]:
		print(i,end=" ")

def imprimirTabuleiro(tabuleiro):
	espaco = 15
	for linha in range(4):
		print(" "*13,end="")
		imprimirLinhaComEspaco(tabuleiro,linha,espaco)
		espaco -= 1
		print()

	espaco =  3
	for linha in range(4,9):
		print(" "*13,end="")
		imprimirLinhaComEspaco(tabuleiro,linha,espaco)
		espaco += 1
		print()

	espaco = 5
	for linha in range(9,13):
		print(" "*13,end="")
		imprimirLinhaComEspaco(tabuleiro,linha,espaco)
		espaco -= 1
		print()

	espaco = 11
	for linha in range(13,17):
		print(" "*13,end="")
		imprimirLinhaComEspaco(tabuleiro,linha,espaco)
		espaco += 1
		print()
