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

    info_frota[nome_navio] = posicao_navio

    return info_frota


