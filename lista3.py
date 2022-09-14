lista = []
i = 0
soma = 0
par = 0
impar = 0
n = int(input('Digite o número de valores a serem inseridos: '))
while i < n:
    v = int(input('Digite o valor a ser inserido: '))
    lista.append(v)
    if v%2 == 0:
        par+=1
    else:
        impar+=1
    soma += lista[i]
    i+=1
media = soma/n
print('O total dos valores é ',soma,' e a média é ',media,', tem',par,' números pares e ',impar,' números ímpares')