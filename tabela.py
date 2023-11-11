
import random
from formulas_cruas import *

###################################CRIANDO A TABELA DINÂMICA
def tabela(n): #n = numero de letras
    linhazinha = ' --- '*(n+1) + '\n'
    tabela = linhazinha
    
    for i in range(n+1):  #numero de linhas
        linha = '|'
        #iniciando a linha - precisa de uma linha do lado, pra fechar os primeiros quadrados
        for palavra in info['especuladas+cores']: #rodando as palavras especuladas
            for iletra in range(len(palavra)):    #rodando as letras da palavra do historico a ´palavra' é uma tabela que corresponde a uma lista com as letras + as cores separadas 
                linha += f' {palavra[iletra]} |'   #colocando as letras na celula

        tabela += linha + '\n' + linhazinha
        
    if info['ntentativas'] != info['tentativas']: #criando as células vazias
        tabela += '|   '*n +'\n'+ linhazinha*info['vidas']

    return tabela
