from palavras import *
import random
from formulas_cruas import *

info = {}
def inicializa(palavras): #cria o dicionário central
    #info['especulada'] = resposta
    info['n']= 6 #número de letra da palavra sorteada 
    info['sorteada'] = random.choice(palavras) #seleção da palavra sorteada
    info['especuladas'] = [] #adicionar a palavra especulada, se ela tiver sido aprovada (se nao foi testada e se está na lista)
    info['tentativas'] = info['n']+1 #numero de vidas
    info['sorteadas'] = [] #lista de sorteadas
    info['resultado'] = indica_posicao(info['sorteada'], info['especulada'])
    info['ntentativas'] = len(info['especuladas'])
    info['vidas'] = info['tentativas'] - info['ntentativas']

    return info


inicializa(palavras)

#n = info['n'] - numero de letras
###################################CRIANDO A TABELA DINÂMICA
def tabela(n):
    linhazinha = ' --- '*(n+1) + '\n'
    tabela = linhazinha
    linha = '|'
    for i in range(n+1):  #numero de linhas
        linha = '|'   #iniciando a linha - precisa de uma linha do lado, pra fechar os primeiros quadrados
        for palavra in info['especuladas']:
            for letra in palavra:
                linha += f' {letra} |'

        tabela += linha + '\n' + linhazinha
        
    if info['ntentativas'] != info['tentativas']: #criando as células vazias
        tabela += '|   '*n +'\n'+ linhazinha*info['vida']

    return tabela

tabela(6)