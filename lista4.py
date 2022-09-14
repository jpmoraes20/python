lista = []
i = 0
soma = 0
acima = 0
while i<100:
    nota = int(input('Digite a nota: '))
    if nota == -1:
        break
    lista.append(nota)
    soma+=nota
    i+=1
media = soma/i
listain = lista[::-1]
for nota in lista:
    if nota>media:
        acima+=1
print ('Foram lidas ',i,' notas: ',lista,', a lista invertida é ',listain,' a soma das notas é: ',soma,', a média é: ',media,' e tiveram ',acima,' notas acima da média')
    