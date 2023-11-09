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



pre_tabela = ''

for i in range(30):
    pre_tabela += str(i)




s = '0123451'

pre_tabela.repalace(s, palavra)


pre_tabelav2 = pre_tabela

for i in range(len(pre_tabelav2)):
    pre_tabelav2.replace(str(i),'      ')


l = []

for letra in palavra:
    l.append(letra)

#função que vai mostrar a interfaço ao player
#Ela recebe dois argumentos, qual a palavra escolhida e quantas tentativas faltam
def interface(string, vez):
    #cria uma lista com cada letra da string
    separadas = list(string)
    


    l = ['      ']*30
    if vez == 6:
        i = 0
    if vez == 5:
        i = 5
    if vez == 4:
        i = 10
    if vez == 3:
        i = 15
    if vez == 2:
        i = 20
    if vez == 1:
        i = 25

    #adiciona na lista cada letra que a string tinha sido dita
    for letra in separadas:
        l[i] = "  " + letra + "   "
        i += 1

    #isso é o que, de fato, vai ser mostrado para o usuário
    msg = f'''
    ┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┓
    ┃  {l[0]} ┃  {l[1]} ┃  {l[2]} ┃  {l[3]} ┃  {l[4]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[5]} ┃  {l[6]} ┃  {l[7]} ┃  {l[8]} ┃  {l[9]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[10]} ┃  {l[11]} ┃  {l[12]} ┃  {l[13]} ┃  {l[14]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[15]} ┃  {l[16]} ┃  {l[17]} ┃  {l[18]} ┃  {l[19]} ┃    
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[20]} ┃  {l[21]} ┃  {l[22]} ┃  {l[23]} ┃  {l[24]} ┃
    ┠━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━╋━━━━━━━━━┨
    ┃  {l[25]} ┃  {l[26]} ┃  {l[27]} ┃  {l[28]} ┃  {l[29]} ┃      
    ┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━┛

    '''
    print(msg)

oi = interface("Termo", 5)