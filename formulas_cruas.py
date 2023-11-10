import random

from palavras import *
especiais = '.;:()=+@!~/|-*><?#$%&_°}{][ªº,'
abc = 'qwertyuiopasdfghjklzxcvbnm'



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

#################################   



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

################################################## DOIS ERROS
#objetivo - criar uma tabela onde eu consiga somente ir adicionando as letras das palavras especuladas
####a: criar um dicionario de 6 termos (= o numero de tentativas), com uma lista de 5 elementos "      " (6espaços) - as chaves de cada termo serao string de 0 a 5
####b: para cada letra, conferir a cor que ela irá receber e a adicionar no dicionario com o endereço: d[numero da linha][posicao da letra na palavra]
########1°: criar um for que percorre número a número da lista do resultado, via contador (i)
###########a°: com base no i, comparar o numero com a sua respectiva cor e armazenar isso na variavel "cor"
###########b°: com base na posição i, selecionar a letra da palavra "resposta" e a anexar dentro da lista da chave que corresponde à sua linha acrescentando a essa letra a variavel 'cor'- 
#              utilizando o str(*numero da tentativa*) para achar a chave correspondente à lista da linha e o i, para identificar o elemento que será substituido dentro da linha

#com base no dicionario criado, atualizar a tabela, com base nas posicoes dos termos dentro das listas dentro dos dicionarios


'''
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
'''

#########################O DIC DE RESULTADOS
dr = {} #dicionario do resultado





printando(0, 'pedra', 'perna')





