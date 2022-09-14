listaog = []
i = 0
while i< 5:
    v = int(input('Digite o valor a ser listado: '))
    listaog.append(v)
    i+=1
listacopia = listaog[::-1]
print('A lista original é ',listaog,' e a lista inversa é ',listacopia)