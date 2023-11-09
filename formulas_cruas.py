from palavras import *
especiais = '.;:()=+@!~/|-*><?#$%&_°}{][ªº,'
abc = 'qwertyuiopasdfghjklzxcvbnm'

#################################   
def inicializa(palavras):
    import random
    retorno = {}

    retorno['n']=len(palavras[0]) #número de letra da palavra sorteada 
    retorno['sorteada'] = random.choice(palavras) #seleção da palavra sorteada
    retorno['especuladas'] = [] #adicionar a palavra especulada, se ela tiver sido aprovada (se nao foi testada e se está na lista)
    retorno['tentativas'] = retorno['n']+1 #numero de vidas

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

d = {}

for i in range(6): #criando as celulas em forma de dicionario
    d[str(i)] = ['      ']














#função que vai mostrar a interfaço ao player
#Ela recebe dois argumentos, qual a palavra escolhida e quantas tentativas faltam
def interface(string, vez):
    #cria uma lista com cada letra da string
    separadas = list(string)
    




    #adiciona na lista cada letra que a string tinha sido dita
    for letra in separadas:
        l[i] = "  " + letra + "   "
        i += 1

    #isso é o que, de fato, vai ser mostrado para o usuário
    msg = f'''
    ┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┓
    ┃  {d[0][0] ┃  d[0][1] ┃  d[0][2] ┃  d[0][3] ┃  d[0][4] ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  d[1][0] ┃  d[2][1] ┃  d[2][2] ┃  d[2][3] ┃  d[1][4] ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  d[2][0] ┃  d[2][1] ┃  d[2][2] ┃  d[2][3] ┃  d[2][4] ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[15]} ┃  {l[16]} ┃  {l[17]} ┃  d[2][3] ┃  d[3][4] ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[20]} ┃  {l[21]} ┃  {l[22]} ┃  {l[23]} ┃  d[4][4] ┃
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[25]} ┃  {l[26]} ┃  {l[27]} ┃  {l[28]} ┃  d[5][4] ┃      
    ┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┛

    '''
    print(msg)

oi = interface("Termo", 5)