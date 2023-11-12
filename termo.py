from palavras import * 
from formulas_cruas import * 

info = inicializa(filtra(lista_de_palavras, 5))
print(info)
#tela_inicial(1)

#loop principal no qual o jogo vai girar entorno
while info['tentativas'] != 0:  #checa se o jogador ainda tem vida

    #input inicial que vai perguntar a palavra ao usuário
    especulada = input(" - Qual palavra sugeres? 🤔")
 
    #remove os espaços em branco 
    especulada = especulada.strip() 

    if not especulada in lista_de_palavras: #confere se a especulada está ou não na lista de palavras viáveis (palavras)
        print('Desculpe-me, mas não conheço essa palavra')

    elif len(especulada) != info["n"]: #confere se a palavra tem realmente 5 letras, se não, pede outra
        print(f'Diga apenas palavras de {info["n"]} letras!!!')

    elif especulada in info['especuladas'] and info['tentativas'] != 6:    #Confere se o usuário já disse essa palavra, caso sim, pede outra
        print('Poxa, você já me disse essa palavra, cite outra!')
    
    ##### A RESPOSTA É VÁLIDA - Caso seja do tamanho correto e inédita, o loop roda normalmente
    else:
        
        info['tentativas'] -= 1     #Desconta-se 1 tentativa das que o usuário tem direito
        info['especuladas'].append(especulada)    #adiciona a resposta do usuário à lista de palavras especuladas
        
        posicao = inidica_posicao( info["sorteada"], especulada)
        ganha = 0 #vai servir pra dizer se o jogador ganhou ou não
        for numero in posicao:
            if numero == 0:
                ganha += 1
            if ganha == 5:
                info['tentativas'] = 0
        print(posicao)
        i = 0
        
        for i in range(len(especulada)):
            cor_letra = cor(posicao[i])
            info['cor+especulada'].append(str(cor_letra) + especulada[i])
            corespeculada1 = " ".join(info['cor+especulada'])
        

        corespeculadaa = " ".join(info['cor+especulada'])
        print('[\033[90m' + corespeculadaa + '\033[90m]')
        info['especuladas+cores'].append(info['cor+especulada'])
        info['cor+especulada'] = []

        #confere se a palavra já não foi sorteada
        if not info['sorteada'] in info["palavras_sorteadas"]:
            info["palavras_sorteadas"].append(info['sorteada'])

