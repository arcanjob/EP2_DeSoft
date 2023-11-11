
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

#################################   



###############
def filtra(palavraas, ndigitos): #FILTRA PALAVRAS PELO TAMANHO, TIRA OS CARACTERES ESPECIAIS E DEVOLVE MINUSCULO

    abc = 'qwertyuiopasdfghjklzxcvbnm'
    
    palavrasv2 = [] #criando uma lista de palavra vazia
    for i in range(len(palavraas)): #rodando a lista de palavras
        palavrasv2.append('') 
        #checando se há um caractere especial
        palavraas[i] = palavraas[i].lower() #deixando todas as palavras minusculas
        for letra in palavraas[i]:
            if letra in abc:  #testando se é caractere especial
                palavrasv2[i] += letra #formando a palavra denovo
        #a palavra já foi formada

    palavrasv3 = []

    for i in range(len(palavrasv2)): #rodando a nova lista de palavras
        if len(palavrasv2[i]) == ndigitos and palavrasv2[i]not in palavrasv3: #palavra com ndigitos e não repetida
            palavrasv3.append(palavrasv2[i])

    return palavrasv3


def cor(numero):
    if int(numero) == 0:
        cor = '\033[92m' #verde - acertou a posição
    if int(numero) == 1:
        cor = '\033[93m' #amarelo - errou a posição
    if int(numero) == 2:
        cor = '\033[90m' #cinza - errou total

    return cor

##################################DICIONARIO COM TUDO



info = {}


def inicializa(palavras_usaveis, nletras, especuladaa): #cria o dicionário central
    global info
    #info['especulada'] = resposta
    info['n']= nletras #número de letra da palavra sorteada 
    n = info['n']
    #print(f'n = {n}')
    #N: OK

    info['sorteada'] = random.choice(palavras_usaveis) #seleção da palavra sorteada
    sorteada = info['sorteada']
    #print(f'sorteada = {sorteada}')
    #SORTEADA: OK 

    
    info['sorteadas'] = [] #lista de sorteadas
    sorteadas = info['sorteadas']
    #print(f'sorteadas = {sorteadas}')
    #SORTEADAS: OK

    info['especulada'] = especuladaa
    especulada = info['especulada']
    #print(f' especulada = {especulada}')
    #ESPECULADA: OK

    #info['especuladas'] = [] #adicionar a palavra especulada, se ela tiver sido aprovada (se nao foi testada e se está na lista)
    #especuladas = info['especuladas']
    #print(f'especuladas = {especuladas}')
    #ESPECULADAS: OK

    info['tentativas'] = info['n']+1 #numero de vidas inicial
    tentativas = info['tentativas']
    #print(f'tentativas = {tentativas}')
    #TENTATIVAS: OK

    info['ntentativas'] = len(info['especuladas'])
    ntentativas = info['ntentativas']
    #print(f'ntentativas = {ntentativas}')
    #TENTATIVAS: OK

    info['vidas'] = info['tentativas'] - info['ntentativas']
    vidas = info['vidas']
    #print(f'vidas = {vidas}')
    #VIDAS: OK

    posicao = inidica_posicao(sorteada, especulada)
    info['resultado'] = posicao
    resultado = info['resultado']
    #print(f'resultado = {resultado}')
    #RESULTADO: OK


    info['cor+especulada'] = []
    corespeculada0 = info['cor+especulada']
    #print(f'corespeculada0 = {corespeculada0}')
    for i in range(len(info['especulada'])):
        cor_letra = cor(info['resultado'][i])
        info['cor+especulada'].append([info['especulada'][i]+str(cor_letra)])
    corespeculada1 = info['cor+especulada']
    #print(f'cor+especulada = {corespeculada1}')
    #COR+ESPECULADA: OK


    #info['especuladas+cores'] = []
    #especuladascores = info['especuladas+cores']
    #print(f'especuladas+cores = {especuladascores}')
    #ESPECULADAS+CORES: OK

    return info



import random


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










































#Define a lista de palavras que vão ser usadas no jogo
info = {}


##################################### 1o PRINT
#mostra as informações inciais do jogo
tela_inicial(3)
nletras = 5
palavras_normais = filtra(palavraas, nletras)


#NUMERO DE VIDAS INICIAIS
print(f'Você tem {nletras+1} tentativa(s)')


# estabelecendo um dicionario x, para rodar a tabela pela primeira vez
info = {}
info['tentativas']= nletras + 1
info['especuladas+cores'] = []
info['ntentativas'] =0
info['vidas']= nletras  +1
info['especuladas'] = [] 

#tabela(nletras)

i = 0 #estabelecendo um contador
#loop principal no qual o jogo vai girar entorno


while info['vidas'] != 0:  #checa se o jogador ainda tem vida
    ########   AVALIANDO SE A RESPOSTA É VALIDA
    #input inicial que vai perguntar a palavra ao usuário
    especulada = input(" - Qual palavra sugeres? 🤔")
    i+=1 #contando as tentativas
    #remove os espaços em branco 
    especulada = especulada.strip() 

    if not especulada in palavraas: #confere se a especulada está ou não na lista de palavras viáveis (palavras)
        print('Desculpe-me, mas não conheço essa palavra')

    elif len(especulada) != nletras:    #confere se a palavra tem realmente 5 letras, se não, pede outra
        print(f'Diga apenas palavras de {nletras} letras!!!')

    elif especulada in info['especuladas'] and info['vidas'] != 6:    #Confere se o usuário já disse essa palavra, caso sim, pede outra
        print('Poxa, você já me disse essa palavra, cite outra!')
    
    ##### A RESPOSTA É VÁLIDA - Caso seja do tamanho correto e inédita, o loop roda normalmente
    else:
        
        info = inicializa(palavras_normais, nletras, especulada)
        
        info['vidas'] -= 1     #Desconta-se 1 tentativa das que o usuário tem direito
        
        info['especuladas'].append(especulada)    #adiciona a resposta do usuário à lista de palavras especuladas
        corespeculadaa = info['cor+especulada']
        print(corespeculadaa)
        info['especuladas+cores'].append(info['cor+especulada'])

        #confere se a palavra já não foi sorteada
        if not info['sorteada'] in info['sorteadas']:
            
            info['sorteadas'].append(info['sorteada'])
            #Confere se as letras da especulada com as da sorteada e diz a sua proximidade com ela
            #(vai servir para colorir as letras e dizer se elas são ou não próximas da paalavra sorteada)
            #posicao = inidica_posicao(info['sorteada'], especulada) #devolve uma lista das posicoes das letras
  
        #print(info)
        
        #print(tabela(nletras))
        
############
#FALTA FAZER A FUNÇÃO QUE VAI FICAR TROCANDO OS TERMOS E COLOCANDO AS LETRAS
#AINDa N SEI COMO FAZER ISSO DE FORMA SIMPLES
#FALTA PENSAR NUMA FORMA DE COLORIR AS LETRAS

   
