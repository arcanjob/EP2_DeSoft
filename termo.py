from palavras import * 
from formulas_cruas import * 

#essa pergunta vai ser importante para que o usuário possa jogar mais de uma vez
repetir = input('''
Olá, vamos jogar ? (SIM ou NAO)                   
''')
sim = ["s", "sim", "si", "yes", "yep"]
if repetir in sim:
    repetir = "sim"
info = {"rumo": repetir.lower()}
if repetir != "sim":
    print("Caso mude de ideia, inicialize o código novamente")

while info["rumo"] == "sim":
    info = inicializa(filtra(lista_de_palavras, 5))
    tela_inicial(1)

    #armazenas as palavras anteriores para o usuário ir vendo
    tela = {
    'l1': "     ",
    'l2': "     ",
    'l3': "     ",
    'l4': "     ",
    'l5': "     ",
    'l6': "     "

    }
    def mensagem_final(nada):
        if ganha == 5:
            print('''    
                \033[92m   MEUS PARABÉNS 
            Você foi um ótimo jogador e conseguiu acertar
            espero que volte para jogar mais vezes    
            ''')
        else:
            
            print('''     
                  \033[31mPoxa,
            Não foi dessa vez, tente treinar mais vezes
            assim, na próxima, você ganha
            ''')
#vai definir a tela que o usuário vai ver com as palavras
    def interface(colorida):
        
        if contador == 0:
            tela['l1'] = colorida.split()
        if contador == 1:
            tela['l2'] = colorida.split()
        if contador == 2:
            tela['l3'] = colorida.split()
        if contador == 3:
            tela['l4'] = colorida.split()
        if contador == 4:
            tela['l5'] = colorida.split()
        if contador == 5:
            tela['l6'] = colorida.split()

        msg = f'''
        \033[90m
        ┏━━━┳━━━┳━━━┳━━━┳━━━┓\033[90m 
        ┃ {tela['l1'][0]} \033[90m┃ {tela['l1'][1]} \033[90m┃ {tela['l1'][2]} \033[90m┃ {tela['l1'][3]} \033[90m┃ {tela['l1'][4]} \033[90m┃
        ┣━━━╋━━━╋━━━╋━━━╋━━━┨\033[90m 
        ┃ {tela['l2'][0]} \033[90m┃ {tela['l2'][1]} \033[90m┃ {tela['l2'][2]} \033[90m┃ {tela['l2'][3]} \033[90m┃ {tela['l2'][4]} \033[90m┃ 
        ┣━━━╋━━━╋━━━╋━━━╋━━━┨\033[90m  
        ┃ {tela['l3'][0]} \033[90m┃ {tela['l3'][1]} \033[90m┃ {tela['l3'][2]} \033[90m┃ {tela['l3'][3]} \033[90m┃ {tela['l3'][4]} \033[90m┃
        ┣━━━╋━━━╋━━━╋━━━╋━━━┨\033[90m 
        ┃ {tela['l4'][0]} \033[90m┃ {tela['l4'][1]} \033[90m┃ {tela['l4'][2]} \033[90m┃ {tela['l4'][3]} \033[90m┃ {tela['l4'][4]} \033[90m┃
        ┣━━━╋━━━╋━━━╋━━━╋━━━┨\033[90m 
        ┃ {tela['l5'][0]} \033[90m┃ {tela['l5'][1]} \033[90m┃ {tela['l5'][2]} \033[90m┃ {tela['l5'][3]} \033[90m┃ {tela['l5'][4]} \033[90m┃
        ┣━━━╋━━━╋━━━╋━━━╋━━━┨\033[90m  
        ┃ {tela['l6'][0]} \033[90m┃ {tela['l6'][1]} \033[90m┃ {tela['l6'][2]} \033[90m┃ {tela['l6'][3]} \033[90m┃ {tela['l6'][4]} \033[90m┃
        ┗━━━┻━━━┻━━━┻━━━┻━━━┛\033[90m 
        '''

        print(msg)

    contador = 0 #vai cintar quantas vezes o jogador jogou o TERMO


    #loop principal no qual o jogo vai girar entorno
    while info['tentativas'] != 0:  #checa se o jogador ainda tem vida
        print(f'''
\033[37mVocê ainda tem \033[92m{info['tentativas']} \033[37mtentativas, use-as bem '''
            )
        #input inicial que vai perguntar a palavra ao usuário
        especulada = input(" - Qual palavra sugeres? 🤔")
        
        #remove os espaços em branco 
        especulada = especulada.strip() 
        if len(especulada) != info["n"]: #confere se a palavra tem realmente 5 letras, se não, pede outra
            print(f'Diga apenas palavras de {info["n"]} letras!!!')

        elif not especulada in lista_de_palavras: #confere se a especulada está ou não na lista de palavras viáveis (palavras)
            print('Desculpe-me, mas não conheço essa palavra')

        elif especulada in info['especuladas'] and info['tentativas'] != 6:    #Confere se o usuário já disse essa palavra, caso sim, pede outra
            print('Poxa, você já me disse essa palavra, cite outra!')
        
        ##### A RESPOSTA É VÁLIDA - Caso seja do tamanho correto e inédita, o loop roda normalmente
        else:
            
            info['tentativas'] -= 1    #Desconta-se 1 tentativa das que o usuário tem direito
            
            info['especuladas'].append(especulada)    #adiciona a resposta do usuário à lista de palavras especuladas
            
            posicao = inidica_posicao( info["sorteada"], especulada)
            ganha = 0 #vai servir pra dizer se o jogador ganhou ou não

            for numero in posicao:
                if numero == 0:
                    ganha += 1
                if ganha == 5:
                    info['tentativas'] = 0
            i = 0
            
            for i in range(len(especulada)):
                cor_letra = cor(posicao[i])
                info['cor+especulada'].append(str(cor_letra) +especulada[i])
                corespeculada1 = " ".join(info['cor+especulada'])
            

            corespeculadaa = " ".join(info['cor+especulada'])
            
            msg = interface(corespeculadaa)
            info['especuladas+cores'].append(info['cor+especulada'])
            info['cor+especulada'] = []

            #confere se a palavra já não foi sorteada
            if not info['sorteada'] in info["palavras_sorteadas"]:
                info["palavras_sorteadas"].append(info['sorteada'])
            contador  += 1 
    #confere se ganhou ou não e dá a resposta final
    print(f"      No fim, a palavra sorteada era \033[92m'{info['sorteada']}'\033[37m...")
    if ganha == 5:
        mensagem_final('')
    else:
        mensagem_final('')
    #permite começar o jogo ou não
    repetir = input('''
\033[37mPara jogar novamente, digite 'SIM'...
Para finalizar, digite 'FIM'                   
''')
    info["rumo"] = repetir.lower()



    
















