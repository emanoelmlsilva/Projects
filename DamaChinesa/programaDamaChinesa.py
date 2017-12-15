from bibliotecaDamaChinesa import *
from GUI import *

numJogadores = menuInicial()
tabuleiro = criarTabuleiro()
nome,peça= nomeDosJogadores(numJogadores)
tabuleiro = adicionarPecas(tabuleiro,numJogadores,peça)
while True:
    for i in range(len(nome)):
        mostrarJogador(numJogadores,peça)
        movimentacao(tabuleiro,nome[i],peça[nome.index(nome[i])])
        #imprimirTabuleiro(tabuleiro)
