matriz = []
soma = 0
for i in range(3) :
    linha = []
    for j in range(5) :
        linha.append(int(input('Digite um número: ')))
        soma+=linha[j]
    matriz.append(linha)

print('A matriz é: ',matriz,' e a soma dos elementos dessa matriz é: ', soma)