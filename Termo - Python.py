import funcoes


print('┏━━━━━━━━━━━━━━━━━━━━━━┓\n┃  Seja bem vindo(a)!  ┃\n┃  Esse é o jogo Termo oooo ┃\n┗━━━━━━━━━━━━━━━━━━━━━━┛')
print('\n')
print(' Regras: \n- Você tem {0} tentativas para acertar uma palavra aleatória de {1} letras.\n- A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n. Azul   : a letra está na posição correta;\n. Amarelo: a palavra tem a letra, mas está na posição errada;\n. Cinza: a palavra não tem a letra.\n- Os acentos são ignorados;\n- As palavras podem possuir letras repetidas.\n \n \n Sorteando uma palavra...\n Já tenho uma palavra! Tente adivinhá-la!\n'.format(6, 5))
print('Você tem {0} tentativa(s)'.format(6))

resp = input(" - Qual palavra sugeres? 🤔.......")

print(funcoes.modelo(2)) #ofoodofd
print(funcoes.TENTATIVAS)
print(TENTATIVAS)
