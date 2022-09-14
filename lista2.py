    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    i = 0
    soma = 0
    m = 0
    while i<15:
        soma += lista[i]
        if lista[i]>10:
            m+=1
        i+=1
    media = soma/15
    print('O total dos valores é ',soma,', a média é ',media,' e existem ',m,' valores acima de 10')
