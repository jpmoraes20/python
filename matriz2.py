matriz=[] 
for i in range(3) :
    linha = []
    for j in range(3) :
        linha.append(int(input('Digite um número: ')))
    matriz.append(linha)
matrix = list(zip(*matriz))
print('\nMatriz:\n')
for i in range(3):
    print(matrix[i])