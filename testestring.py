frase = 'Python é a melhor linguagem'
indice = 0
while indice > -1:
    indice = frase.find('o', indice)
    if indice >= 0:
        print('Índice: ', indice)
        indice +=1