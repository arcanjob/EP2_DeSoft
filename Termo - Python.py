from palavras import *
from formulas_cruas import *

#Define a lista de palavras que vão ser usadas no jogo
palavras_normais = filtra(palavras, 5)


#inicializa o dicionario com as informações iniciais
info = inicializa(palavras_normais)


#para marcar as palavras que já foram sorteadas.
sorteadas = []

#mostra as informações inciais do jogo
print('''
     ┏━━━━━━━━━━━━━━━━━━━━━━┓
     ┃  Seja bem vindo(a)!  ┃
     ┃  Esse é o jogo Termo ┃
     ┗━━━━━━━━━━━━━━━━━━━━━━┛
      ''')
#print('\n')
print('''
 Regras: Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.
 - A cada tentativa, a palavra testada terá suas letras coloridas conforme:
 . Azul  : a letra está na posição correta;
 . Amarelo: a palavra tem a letra, mas está na posição errada;
 . Cinza: a palavra não tem a letra.
 - Os acentos são ignorados;
 - As palavras podem possuir letras repetidas.
 
  Sorteando uma palavra...
  Já tenho uma palavra! Tente adivinhá-la!
''')

#informa a quantidade de tentativas restantes ao usuário
print('Você tem {0} tentativa(s)'.format(6))

#loop principal no qual o jogo vai girar entorno

while info['tentativas'] != 0:
    #input inicial que vai perguntar a palavra ao usuário
    resposta = input(" - Qual palavra sugeres? 🤔")
    #remove os espaços em branco
    resposta = resposta.strip() 

    #confere se a especulada está ou não na lista de palavras viáveis
    if not resposta in palavras:
        print('Desculpe-me, mas não conheço essa palavra')
    #confere se a palavra tem realmente 5 letras, se não, pede outra
    elif len(resposta) != 5:
        print('Diga apenas palavras de 5 letras!!!')

    #Confere se o usuário já disse essa palavra, caso sim, pede outra
    elif resposta in info['especuladas'] and info['tentativas'] != 6:
        print('Poxa, você já me disse essa palavra, cite outra!')

    #Caso seja do tamanho correto e inédita, o loop roda normalmente
    else:
    
        #Desconta-se 1 tentativa das que o usuário tem direito
        info['tentativas'] -= 1 
        
        #adiciona a resposta do usuário à lista de palavras especuladas
        info['especuladas'].append(resposta)
        
        #confere se a palavra já não foi sorteada
        if not info['sorteada'] in sorteadas:
            
            #Confere se as letras da especulada com as da sorteada e diz a sua proximidade com a tal
            #vai servir para colorir as letras e dizer se elas são ou não próximas da paalavra sorteada
            posicao = inidica_posicao(info['sorteada'], resposta)

        sorteadas.append(info['sorteada'])
        



############
#FALTA FAZER A FUNÇÃO QUE VAI FICAR TROCANDO OS TERMOS E COLOCANDO AS LETRAS
#AINDa N SEI COMO FAZER ISSO DE FORMA SIMPLES



      

'''
┏━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┓
┃  {A} ┃  {B} ┃  {C} ┃  {C} ┃  {D} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃  {E} ┃  {F} ┃  {G} ┃  {H} ┃  {I} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃  {J} ┃  {K} ┃  {L} ┃  {M} ┃  {N} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃  {O} ┃  {P} ┃  {Q} ┃  {R} ┃  {S} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃  {T} ┃  {U} ┃  {V} ┃  {W} ┃  {X} ┃  
┗━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┛

'''