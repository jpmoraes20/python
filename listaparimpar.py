listapar = []
listaimpar = []
n = int(input('Digite o primeiro valor: '))
m = int(input('Digite o último valor: '))
i = n
while i<=m:
    if i%2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)
    i+=1
print('Números pares: ',listapar,', números ímpares: ',listaimpar)