grupo = int(input('Qual o tamanho do grupo? '))
pessoas = 0
m = 0
while pessoas < grupo:
    idade = int(input('Digite a sua idade: '))
    m += idade
    pessoas +=1
m = m/pessoas
if m < 25:
    print('O grupo é majoritariamente jovem, a média de idade é ',m)
elif m < 60:
    print('O grupo é majoritariamente adulto, a média de idade é ',m)
elif m > 60:
    print('O grupo é majoritariamente idoso, a média de idade é ',m)
