matriz = []

for i in range(3):
    linha = []
    for j in range(6):
        linha.append(int(input('Digite um número: ')))
    matriz.append(linha)
maior = max([valor for linha in matriz for valor in linha])
menor = min([valor for linha in matriz for valor in linha])

maior_linha = matriz.index(max(matriz))
maior_coluna = matriz[maior_linha].index(max(matriz[maior_linha]))
menor_linha = matriz.index(min(matriz))
menor_coluna = matriz[menor_linha].index(min(matriz[menor_linha]))
maiorin = f'({maior_linha}, {maior_coluna})'
menorin = f'({menor_linha}, {menor_coluna})'
print('A matriz é ',matriz,', o maior número é ', maior,' e está na posição ',maiorin,' e o menor é ',menor,' e está na posição ',menorin)
