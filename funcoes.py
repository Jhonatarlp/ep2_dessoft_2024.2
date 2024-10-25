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


def faz_jogada(tabuleiro, linha, coluna):
    
    if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
        if tabuleiro[linha][coluna] == 1:
            tabuleiro[linha][coluna] = 'X'  
        else:
            tabuleiro[linha][coluna] = '-' 

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
                    break
            if afundado:
                afundados += 1
    return afundados



def posicao_valida(info_frota, linha, coluna, orientacao, tamanho):
    navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in navio:
        if posicao[0] > 9:
            return False
        if posicao[1] > 9:
            return False
        for lista_navios in info_frota.values():
            for barco in lista_navios:
                for casa in barco:
                    if posicao == casa:
                        return False
    return True



def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
