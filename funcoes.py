def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes_lista = []
    if orientacao == 'vertical':
        for l in range(linha,linha+tamanho):
            posicoes_lista.append([l,coluna])
    elif orientacao == 'horizontal':
        for c in range(coluna, coluna+tamanho):
            posicoes_lista.append([linha,c])
    return posicoes_lista
