import random

from palavras import *

especiais = '.;:()=+@!~/|-*><?#$%&_°}{][ªº,'
abc = 'qwertyuiopasdfghjklzxcvbnm'

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

def inidica_posicao(sorteada, especulada):

    if not len(sorteada) == len(especulada):
        return []
    
    retorno = []

    for ile in range(len(especulada)): #ile = posição da letra
        if especulada[ile] not in sorteada: #a letra não está na sorteada
            retorno.append(2)
        elif especulada[ile] == sorteada[ile]: #letra no lugar certo
            retorno.append(0)
        
        else:
            retorno.append(1) #letra presente, mas no lugar errado
    
    return retorno        


#################################  DOIS ERROS 
   
###############

def filtra(palavras, numero):
    print(palavras)
    normal = []
    especiais = "?!.,"
    
    for palavra in palavras:
       
        if len(palavra) == numero:
            corrigida = palavra.lower()
            if not corrigida in normal:
                normal.append(corrigida)
    return normal
