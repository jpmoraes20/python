matriz = []
p = []
par = 0
media = 0
for i in range(2) :
    linha = []
    p1 = p
    s = p1
    for j in range(4) :
        linha.append(int(input('Digite um número: ')))
    pares = [x for x in linha if x%2==0]
    p.append(pares)
    matriz.append(linha)
    for m in linha:
            if m%2 ==0:
                par+=1
                media+=m
media = media/par


print('A matriz é: ',matriz,', existem ',par,' números pares, e a média deles é ',media, ', tem ',len(p[0]),' pares na primeira linha e ',len(p[1]),' pares na segunda linha')