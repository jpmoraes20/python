matriz = []
soma = 0
media = 0
msala = 0
for i in range(2):
    linha = []
    for j in range(5):
        linha.append(int(input('Digite uma nota: ')))
        soma += linha[j]
        media += linha[j]
    media=media/(j+1)
    if media > 6:
        print('Aluno ',(i+1),' aprovado, média: ',media)
    elif media < 6:
        print('Aluno ',(i+1),' reprovado, média: ',media)
    matriz.append(linha)
    msala += media
    media=0
alu = 0
for m in matriz:
    alu+=1
msala = msala/alu
print('A média da sala foi ', msala)