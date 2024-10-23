from funcoes import *

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

print(info_frota)