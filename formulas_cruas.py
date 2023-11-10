import random

from palavras import *
especiais = '.;:()=+@!~/|-*><?#$%&_°}{][ªº,'
abc = 'qwertyuiopasdfghjklzxcvbnm'

#################################   
info = {}

    info['n']=len(palavras[0]) #número de letra da palavra sorteada 
    info['sorteada'] = random.choice(palavras) #seleção da palavra sorteada
    info['especuladas'] = [] #adicionar a palavra especulada, se ela tiver sido aprovada (se nao foi testada e se está na lista)
    info['tentativas'] = info['n']+1 #numero de vidas
    info['sorteadas'] = [] #lista de sorteadas
    info['especulada'] = 
    info['resultado'] = indica_posicao(info['sorteada'], info['especulada'])

    return retorno

#################################   

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


###############
def filtra(palavras, ndigitos): #FILTRA PALAVRAS PELO TAMANHO, TIRA OS CARACTERES ESPECIAIS E DEVOLVE MINUSCULO

    abc = 'qwertyuiopasdfghjklzxcvbnm'
    
    palavrasv2 = [] #criando uma lista de palavra vazia
    for i in range(len(palavras)): #rodando a lista de palavras
        palavrasv2.append('') 
        #checando se há um caractere especial
        palavras[i] = palavras[i].lower() #deixando todas as palavras minusculas
        for letra in palavras[i]:
            if letra in abc:  #testando se é caractere especial
                palavrasv2[i] += letra #formando a palavra denovo
        #a palavra já foi formada

    palavrasv3 = []

    for i in range(len(palavrasv2)): #rodando a nova lista de palavras
        if len(palavrasv2[i]) == ndigitos and palavrasv2[i]not in palavrasv3: #palavra com ndigitos e não repetida
            palavrasv3.append(palavrasv2[i])

    return palavrasv3


##############################################PRINT
#####VAI LÁ PRA CIMA
d = {}

for i in range(6): #criando as celulas em forma de dicionario - PARA A INTERFACE
    d[str(i)] = ['      ']
###


def printando(info): # vai dar a resposta
    
    resultado = ''
    for i in range(5):
        resultado += str(info['sorteada'][i])

    print(resultado)
    #def cor(nada):
    i = 6
    while i > 6:
        print(resultado[i])
        if int(resultado[i]) == 0:
            cor = '\033[92m' #verde - acertou a posição
        if int(resultado[i]) == 1:
            cor = '\033[93m' #amarelo - errou a posição
        if int(resultado[i]) == 2:
            cor = '\033[90m' #cinza - errou total
        d[str(ntentativa)] = tentativa[i] + cor

        print(tentativa[i])
        i -= 1

    
    #isso é o que, de fato, vai ser mostrado para o usuário
    msg = f'''
    ┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┓
    ┃  {d['0'][0]} ┃  {d['0'][1]} ┃  {d['0'][2]} ┃  {d['0'][3]} ┃  {d['0'][4]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {d['1'][0]} ┃  {d['2'][1]} ┃  {d['2'][2]} ┃  {d['2'][3]} ┃  {d['1'][4]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {d['2'][0]} ┃  {d['2'][1]} ┃  {d['2'][2]} ┃  {d['2'][3]} ┃  {d['2'][4]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {d['3'][0]} ┃ {d['3'][1]} ┃  {d['3'][2]} ┃  {d['3'][3]} ┃  {d['3'][4]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {d['4'][0]} ┃  {d['4'][1]}┃  {d['4'][2]} ┃  {d['4'][3]} ┃  {d['4'][4]} ┃
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {d['5'][0]} ┃  {d['5'][1]} ┃  {d['5']['2']} ┃  {d['5'][3]} ┃  {d['5'][4]} ┃      
    ┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┛

    '''
    
    print(msg)


#########################O DIC DE RESULTADOS
dr = {} #dicionario do resultado





printando(0, 'pedra', 'perna')





