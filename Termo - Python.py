#from palavras import *
#from letras_e_caracteres_especiais import *


print('┏━━━━━━━━━━━━━━━━━━━━━━┓\n┃  Seja bem vindo(a)!  ┃\n┃  Esse é o jogo Termo ┃\n┗━━━━━━━━━━━━━━━━━━━━━━┛')
print('\n')
print(' Regras: \n- Você tem {0} tentativas para acertar uma palavra aleatória de {1} letras.\n- A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n. Azul   : a letra está na posição correta;\n. Amarelo: a palavra tem a letra, mas está na posição errada;\n. Cinza: a palavra não tem a letra.\n- Os acentos são ignorados;\n- As palavras podem possuir letras repetidas.\n \n \n Sorteando uma palavra...\n Já tenho uma palavra! Tente adivinhá-la!\n'.format(6, 5))
print('Você tem {0} tentativa(s)'.format(6))

#resp = input(" - Qual palavra sugeres? 🤔")

#normaliza a palavra que o usuário respondeu
#escolhida = resp.lower()



print('''
┏━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┓
┃  {0} ┃  {1} ┃  {2} ┃  {3} ┃  {4} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃  {5} ┃  {6} ┃  {7} ┃  {8} ┃  {9} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃ {10} ┃ {11} ┃ {12} ┃ {13} ┃ {14} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃ {15} ┃ {16} ┃ {17} ┃ {18} ┃ {19} ┃  
┠━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┨
┃ {20} ┃ {21} ┃ {22} ┃ {23} ┃ {24} ┃  
┗━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┛

'''.format())