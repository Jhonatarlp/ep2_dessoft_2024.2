from funcoes import *
import random
random.seed(2)

jogando = True

while jogando:

    info_frota = {
        "porta-aviões": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": [],
    }    

    pa_cont = 0
    while pa_cont < 1:
        print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('Orientação: [1] Vertical [2] Horizontal '))
        orientacao = 'vertical' if orientacao == 1 else 'horizontal'

        if posicao_valida(info_frota, linha, coluna, orientacao, 4):
            pa_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 4)
            info_frota["porta-aviões"].append(navio)
        else:
            print('Esta posição não está válida!')

    nt_cont = 0
    while nt_cont < 2:
        print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('Orientação: [1] Vertical [2] Horizontal '))
        orientacao = 'vertical' if orientacao == 1 else 'horizontal'

        if posicao_valida(info_frota, linha, coluna, orientacao, 3):
            nt_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 3)
            info_frota["navio-tanque"].append(navio)
        else:
            print('Esta posição não está válida!')

    c_cont = 0
    while c_cont < 3:
        print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('Orientação: [1] Vertical [2] Horizontal '))
        orientacao = 'vertical' if orientacao == 1 else 'horizontal'

        if posicao_valida(info_frota, linha, coluna, orientacao, 2):
            c_cont += 1
            navio = define_posicoes(linha, coluna, orientacao, 2)
            info_frota["contratorpedeiro"].append(navio)
        else:
            print('Esta posição não está válida!')

    s_cont = 0
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
            [[2, 7]], [[0, 6]], [[9, 7]], [[7, 6]]
        ]
    }
    
    total_navios_oponente = sum(len(lista) for lista in frota_oponente.values())
    tabuleiro_oponente = posiciona_frota(frota_oponente)
    tabuleiro_jogador = posiciona_frota(info_frota)
    ataques = []
    ataques_oponente = []
    
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        
        jogada_jogador_linha = int(input("Jogador, qual linha deseja atacar? "))
        while jogada_jogador_linha > 9 or jogada_jogador_linha < 0:
            print('Linha inválida!')
            jogada_jogador_linha = int(input("Jogador, qual linha deseja atacar? "))

        jogada_jogador_coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while jogada_jogador_coluna > 9 or jogada_jogador_coluna < 0:
            print('Coluna inválida!')
            jogada_jogador_coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if [jogada_jogador_linha, jogada_jogador_coluna] in ataques:
            print(f'A posição linha {jogada_jogador_linha} e coluna {jogada_jogador_coluna} já foi informada anteriormente!')
            continue

        ataques.append([jogada_jogador_linha, jogada_jogador_coluna])
        faz_jogada(tabuleiro_oponente, jogada_jogador_linha, jogada_jogador_coluna)

        if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando = False
            break

        while True:
            ataque_linha_oponente = random.randint(0, 9)
            ataque_coluna_oponente = random.randint(0, 9)

            if [ataque_linha_oponente, ataque_coluna_oponente] not in ataques_oponente:
                ataques_oponente.append([ataque_linha_oponente, ataque_coluna_oponente])
                print(f"Seu oponente está atacando na linha {ataque_linha_oponente} e coluna {ataque_coluna_oponente}")
                faz_jogada(tabuleiro_jogador, ataque_linha_oponente, ataque_coluna_oponente)
                break

        if afundados(info_frota, tabuleiro_jogador) == sum(len(lista) for lista in info_frota.values()):
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
            break
        else:
            print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))