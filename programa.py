from funcoes import *
jogando = True

while jogando:

    info_frota = {
        "porta-aviões":[],
        "navio-tanque":[],
        "contratorpedeiro":[],
        "submarino": [],
    }    

    pa_cont = 0 #contador de porta-avioes
    while pa_cont < 1:
        print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('Orientação: [1]Vertical [2]Horizontal >'))
        if orientacao == 1: orientacao = 'vertical'
        elif orientacao == 2: orientacao = 'horizontal'

        if posicao_valida(info_frota, linha, coluna, orientacao, 4):
            pa_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 4)
            info_frota["porta-aviões"].append(navio)
        else:
            print('Esta posição não está válida!')


    nt_cont = 0 #contador de navio-tanque
    while nt_cont < 2:
        print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('Orientação: [1]Vertical [2]Horizontal >'))
        if orientacao == 1: orientacao = 'vertical'
        elif orientacao == 2: orientacao = 'horizontal'

        if posicao_valida(info_frota, linha, coluna, orientacao, 3):
            nt_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 3)
            info_frota["navio-tanque"].append(navio)
        else:
            print('Esta posição não está válida!')


    c_cont = 0 #contador de contratorpedeiro
    while c_cont < 3:
        print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('Orientação: [1]Vertical [2]Horizontal >'))
        if orientacao == 1: orientacao = 'vertical'
        elif orientacao == 2: orientacao = 'horizontal'

        if posicao_valida(info_frota, linha, coluna, orientacao, 2):
            c_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 2)
            info_frota["contratorpedeiro"].append(navio)
        else:
            print('Esta posição não está válida!')

    s_cont = 0 #contador de submarino
    while s_cont < 4:
        print('Insira as informações referentes ao navio submarino que possui tamanho 1')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = 'vertical'

        if posicao_valida(info_frota, linha, coluna, orientacao, 1):
            s_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 1)
            info_frota["submarino"].append(navio)
        else:
            print('Esta posição não está válida!')


    frota_oponente = {
        'porta-aviões': [
            [[9, 1], [9, 2], [9, 3], [9, 4]]
        ],
        'navio-tanque': [
            [[6, 0], [6, 1], [6, 2]],
            [[4, 3], [5, 3], [6, 3]]
        ],
        'contratorpedeiro': [
            [[1, 6], [1, 7]],
            [[0, 5], [1, 5]],
            [[3, 6], [3, 7]]
        ],
        'submarino': [
            [[2, 7]],
            [[0, 6]],
            [[9, 7]],
            [[7, 6]]
        ]
    }
    pos_total = 0
    for listas in frota_oponente.values():
        for navio in listas:
            for casas in navio:
                pos_total += 1
            

    tabuleiro_oponente = posiciona_frota(frota_oponente)
    jogador = posiciona_frota(info_frota)
    ataques = []
    

    print(monta_tabuleiros(jogador, tabuleiro_oponente))

    while True:
        jogada_jogador_linha = int(input("Jogador, qual linha deseja atacar? "))
        while jogada_jogador_linha > 9 or jogada_jogador_linha < 0:
            print('Linha inválida!')
            jogada_jogador_linha = int(input("Jogador, qual linha deseja atacar? "))


        jogada_jogador_coluna = int(input("Jogador, qual Coluna deseja atacar? "))
        while jogada_jogador_coluna > 9 or jogada_jogador_coluna < 0:
            print('Coluna inválida!')
            jogada_jogador_coluna = int(input("Jogador, qual Coluna deseja atacar? "))                 


        if [jogada_jogador_linha,jogada_jogador_coluna] in ataques:
            print(f'A posição linha {jogada_jogador_linha} e coluna {jogada_jogador_coluna} já foi informada anteriormente!')
            continue
            
        ataques.append([jogada_jogador_linha, jogada_jogador_coluna])

        jogada_momento = faz_jogada(tabuleiro_oponente, jogada_jogador_linha, jogada_jogador_coluna)
        tabuleiro_oponente = jogada_momento

        if afundados(frota_oponente, tabuleiro_oponente) == pos_total:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
            break
        else:
            print(monta_tabuleiros(jogador, tabuleiro_oponente))