def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes_lista = []
    if orientacao == 'vertical':
        for l in range(linha,linha+tamanho):
            posicoes_lista.append([l,coluna])
    elif orientacao == 'horizontal':
        for c in range(coluna, coluna+tamanho):
            posicoes_lista.append([linha,c])
    return posicoes_lista



def preenche_frota(info_frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in info_frota:
        info_frota[nome_navio].append(posicao_navio)
    else:
        info_frota[nome_navio] = [posicao_navio]
    
    return info_frota



def faz_jogada(tabuleiro, linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro



def posiciona_frota(info_frota):
    tabuleiro = []
    for l in range(10):
        x = []
        for c in range(10):
            x.append(0)
        tabuleiro.append(x)

    for posicao in info_frota.values():
        for casas in posicao:
            for pos in casas:
                lin = pos[0]
                col = pos[1]
                tabuleiro[lin][col] = 1
                
    return tabuleiro



def afundados(frota, tabuleiro):
    afundados = 0
    for lista in frota.values():
        for navio in lista:
            afundado = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundado = False
            if afundado:
                afundados += 1

    return afundados