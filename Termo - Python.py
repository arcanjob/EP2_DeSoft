import funcoes
from funcoes import TENTATIVAS

print('┏━━━━━━━━━━━━━━━━━━━━━━┓\n┃  Seja bem vindo(a)!  ┃\n┃  Esse é o jogo Termo ┃\n┗━━━━━━━━━━━━━━━━━━━━━━┛')
print('\n')
print(' Regras: \n- Você tem 6 tentativas para acertar uma palavra aleatória de 5 letras.\n- A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n. Azul   : a letra está na posição correta;\n. Amarelo: a palavra tem a letra, mas está na posição errada;\n. Cinza: a palavra não tem a letra.\n- Os acentos são ignorados;\n- As palavras podem possuir letras repetidas.\n \n \n Sorteando uma palavra...\n Já tenho uma palavra! Tente adivinhá-la!\n')
print('Você tem {0} tentativa(s)'.format(6))
resp = input(" - Qual palavra sugeres? 🤔.......")

print(funcoes.modelo(2))
print(funcoes.TENTATIVAS)
print(TENTATIVAS)
