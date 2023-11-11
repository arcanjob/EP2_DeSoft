
import random
from formulas_cruas import *

def tela_inicial(nada):
    
    print('''
        ┏━━━━━━━━━━━━━━━━━━━━━━┓
        ┃  Seja bem vindo(a)!  ┃
        ┃                      ┃
        ┃ Esse é o jogo termo  ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━┛
        ''')
    #REGRAS
    print('''
    Regras: 
        Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.
        - A cada tentativa, essa palavra testada terá suas letras coloridas conforme:
        . VERDE  : a letra está na posição correta;
        . AMARELO: a palavra tem a letra, mas está na posição errada;
        . CINZA: a palavra não tem a letra.
        - Os acentos são ignorados;
        - As palavras podem possuir letras repetidas.
    
    Sorteando uma palavra...
    Já tenho uma palavra! vamos, tente adivinhá-la!
    ''')

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
