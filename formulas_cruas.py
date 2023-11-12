sorteada = []

#define a tela inicial com as regras do jogo para o jogador
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
        . \033[92mVERDE  \033[37m: a letra está na posição correta;
        . \033[93mAMARELO\033[37m: a palavra tem a letra, mas está na posição errada;
        . \033[90mCINZA\033[37m: a palavra não tem a letra.
        - Os acentos são ignorados;
        - As palavras podem possuir letras repetidas;
        - CUIDADO!!!, digite apenas palavras válidas
    Sorteando uma palavra...
    Já tenho uma palavra! vamos, tente adivinhá-la!
    ''')

def inidica_posicao(sorteada, especulada):
    sorteada = sorteada.lower()
    especulada = especulada.lower()
    
    lista = [0]*len(sorteada)
    
    if len(sorteada) != len(especulada):
        return []
    else:
        for i in range(len(especulada)):
            
            if especulada[i] in sorteada:
                lista[i] = 1
                if especulada[i] == sorteada[i]:
                    lista[i] = 0
            elif especulada[i] not in sorteada:
                lista[i] = 2
            
           
    return lista
            

def inicializa(palavras):
    import random
    info = {}
    n = len(palavras[0])
    a = 0
    while a == 0:
        sorteio = random.choice(palavras)
        if not sorteio in sorteada:   
            info['sorteada'] = sorteio
            a += 1
    info["palavras_sorteadas"] = []
    info["n"] = n 
    info['especuladas'] = []
    info['tentativas'] = n + 1
    info["cor+especulada"] = []
    info["especuladas+cores"] = []
    info["rumo"] = 'termo'
    sorteada.append(info['sorteada'])
    return info


def filtra(palavras, numero):
    normal = []
    especiais = "?!.,"
    
    for palavra in palavras:
    
        if len(palavra) == numero:
            corrigida = palavra.lower()
            if not corrigida in normal:
                normal.append(corrigida)

    return normal
    
#esssa função define a cor da letra na interface visual
def cor(numero):
    if int(numero) == 0:
        cor = '\033[92m' #verde - acertou a posição
    if int(numero) == 1:
        cor = '\033[93m' #amarelo - errou a posição
    if int(numero) == 2:
        cor = '\033[90m' #cinza - errou total

    return cor 

