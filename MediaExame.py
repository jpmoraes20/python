n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

if m >=7:
    print('Você foi aprovado e sua média foi ', m)
elif m<7 and m>=4:
    print('Você está de exame e sua média foi ', m )
elif m<4:
    print('Você foi reprovado e sua média foi ', m )
