
import random
from formulas_cruas import *

#definindo a cor
def cor(numero):
    if int(numero) == 0:
        cor = '\033[92m' #verde - (acertou a posição)
    if int(numero) == 1:
        cor = '\033[93m' #amarelo - (errou a posição)
    if int(numero) == 2:
        cor = '\033[90m' #cinza - (errou total)

    return cor

##################################DICIONARIO COM TUDO

info = {}

def inicializa(palavras_usaveis, nletras, especulada): #cria o dicionário central
    global info
    #info['especulada'] = resposta
    info['n']= nletras #número de letra da palavra sorteada 

    info['sorteada'] = random.choice(palavras_usaveis) #seleção da palavra sorteada
    info['sorteadas'] = [] #lista de sorteadas

    info['especulada'] = especulada
    info['especuladas'] = [] #adicionar a palavra especulada, se ela tiver sido aprovada (se nao foi testada e se está na lista)
    
    
    info['tentativas'] = info['n']+1 #numero de vidas inicial
    info['ntentativas'] = len(info['especuladas'])
    info['vidas'] = info['tentativas'] - info['ntentativas']
    


    info['resultado'] = inidica_posicao(info['sorteada'], info['especulada'])
    info['resultado'] = [1,1,1,1,1,1]
    info['cor+especulada'] = []
    for i in range(len(info['especulada'])):
        cor_letra = cor(info['resultado'][i])
        info['cor+especulada'].append([info['especulada'][i]+cor_letra])
        

    info['especuladas+cores'] = []

    return info

print(inicializa(palavraas, 5, "vidro"))


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
