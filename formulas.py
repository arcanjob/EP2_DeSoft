#FUNÇÕES QUE VÃO SER USADAS NO TERMO
def filtra(palavras, numero):
    print(palavras)
    normal = []
    especiais = "?!.,"
    
    for palavra in palavras:
       
        if len(palavra) == numero:
            corrigida = palavra.lower()
            if not corrigida in normal:
                normal.append(corrigida)
    return normal

#################################   
    
def inicializa(palavras):
    import random
    dic = {}
    n = len(palavras[0])
    dic['sorteada'] = random.choice(palavras)
    dic["n"] = n 
    dic['especuladas'] = []
    dic['tentativas'] = n + 1
    return dic

#################################   

def inidica_posicao(sorteada, especulada):
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