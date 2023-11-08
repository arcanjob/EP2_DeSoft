from palavras import *
from formulas_cruas import *

#Define a lista de palavras que vão ser usadas no jogo
palavras_normais = filtra(palavras, 5)


#inicializa o dicionario com as informações iniciais
info = inicializa(palavras_normais)


#para marcar as palavras que já foram sorteadas.
sorteadas = []


#mostra as informações inciais do jogo
print('┏━━━━━━━━━━━━━━━━━━━━━━┓\n┃  Seja bem vindo(a)!  ┃\n┃  Esse é o jogo Termo ┃\n┗━━━━━━━━━━━━━━━━━━━━━━┛')
print('\n')
print(' Regras: \n- Você tem {0} tentativas para acertar uma palavra aleatória de {1} letras.\n- A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n. Azul   : a letra está na posição correta;\n. Amarelo: a palavra tem a letra, mas está na posição errada;\n. Cinza: a palavra não tem a letra.\n- Os acentos são ignorados;\n- As palavras podem possuir letras repetidas.\n \n \n Sorteando uma palavra...\n Já tenho uma palavra! Tente adivinhá-la!\n'.format(6, 5))
print('Você tem {0} tentativa(s)'.format(6))


#input inicial que vai perguntar a palavra ao usuário
resposta = input(" - Qual palavra sugeres? 🤔")


#loop principal no qual o jogo vai girar entorno
while info['tentativas'] != 0:
    
    #confere se a especulada está ou não na lista de palavras viáveis
    if not resposta in palavras:
        print('Desculpe-me, mas não conheço essa palavra')
    #confere se a palavra tem realmente 5 letras, se não, pede outra
    if len(resposta) != 5:
        print('Diga apenas palavras de 5 letras!!!')

    #Confere se o usuário já disse essa palavra, caso sim, pede outra
    if resposta in info['especuladas']:
        print('Poxa, você já me disse essa palavra, cite outra!')
    
    #Caso seja do taamnho correto e inédita, o loop roda normalmente
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