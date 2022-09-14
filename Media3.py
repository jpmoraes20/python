alu = 0
ap = 0
rep = 0
ms = 0
maior = 0
menor = 10
while alu < 10:
    mat = input('Digite o número da matrícula do aluno: ')
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    n3 = float(input('Digite a nota 3: '))
    m = (n1+n2+n3)/3
    ms += m
    if m > maior:
        maior = m
    else:
        maior = maior
    if m < menor:
        menor = m
    else:
        menor = menor
    f = float(input('Digite a frequência(%): '))
    if m >= 6 and f >= 75:
        print('Aluno ',mat,' aprovado com ',f,'% de frequência e média ', m)
        ap+=1
    else :
        print('Aluno ',mat,' reprovado com ',f,'% de frequência e média ', m)
        rep+=1
    alu+=1
print('A média da turma foi', ms/10,' e tiveram ',ap,' alunos aprovados e',rep,' alunos reprovados, a maior média da sala foi', maior,' e a menor foi ',menor)