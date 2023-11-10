from palavras import *
from formulas_cruas import *
import random

#Define a lista de palavras que vão ser usadas no jogo




##################################### 1o PRINT
#mostra as informações inciais do jogo
print('''
     ┏━━━━━━━━━━━━━━━━━━━━━━┓
     ┃  Seja bem vindo(a)!  ┃
     ┃  Esse é o jogo Termo ┃
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

nletras = 5

palavras_normais = filtra(palavras, nletras)

#NUMERO DE VIDAS INICIAIS
print(f'Você tem {nletras+1} tentativa(s)')

# estabelecendo um dicionario x, para rodar a tabela pela primeira vez
info = {'tentativas': nletras+1;    'especuladas+cores':[];    'ntentativas'=0; 'vidas':nletras } 

print(tabela(nletras))

i = 0 #estabelecendo um contador
#loop principal no qual o jogo vai girar entorno

while info['tentativas'] != 0:  #checa se o jogador ainda tem vida
    ########   AVALIANDO SE A RESPOSTA É VALIDA
    #input inicial que vai perguntar a palavra ao usuário
    especulada = input(" - Qual palavra sugeres? 🤔")
    i+=1 #contando as tentativas
    #remove os espaços em branco 
    especulada = especulada.strip() 

    
    if not especulada in palavras: #confere se a especulada está ou não na lista de palavras viáveis (palavras)
        print('Desculpe-me, mas não conheço essa palavra')

    
    elif len(especulada) != nletras:    #confere se a palavra tem realmente 5 letras, se não, pede outra
        print('Diga apenas palavras de 5 letras!!!')

    
    elif especulada in info['especuladas'] and info['tentativas'] != 6:    #Confere se o usuário já disse essa palavra, caso sim, pede outra
        print('Poxa, você já me disse essa palavra, cite outra!')

    
    ##### A RESPOSTA É VÁLIDA - Caso seja do tamanho correto e inédita, o loop roda normalmente
    else:
        
        inicializa(palavras_normais, nletras, especulada)


        #info['especulada'] = especulada #atualiza o valor da chave especulada
        #info['tentativas'] -= 1     #Desconta-se 1 tentativa das que o usuário tem direito
        
        
        info['especuladas'].append(especulada)    #adiciona a resposta do usuário à lista de palavras especuladas
        info['especuladas+cores'].append(info['cor+especulada'])



        #confere se a palavra já não foi sorteada
        if not info['sorteada'] in info['sorteadas']:
            
            info['sorteadas'].append(info['sorteada'])
            #Confere se as letras da especulada com as da sorteada e diz a sua proximidade com ela
            #(vai servir para colorir as letras e dizer se elas são ou não próximas da paalavra sorteada)
            posicao = inidica_posicao(info['sorteada'], especulada) #devolve uma lista das posicoes das letras
        oi = printando(especulada) #printa a resposta por tentativa
        

############
#FALTA FAZER A FUNÇÃO QUE VAI FICAR TROCANDO OS TERMOS E COLOCANDO AS LETRAS
#AINDa N SEI COMO FAZER ISSO DE FORMA SIMPLES
#FALTA PENSAR NUMA FORMA DE COLORIR AS LETRAS

   
