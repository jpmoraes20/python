''' JOGO DE CRAPS: Trata - se de um jogo de sorte onde são lançados dois dados e é feita um aposta no resultado da soma desses dados
    Regras: Para ganhar no primeiro lançamento, é necessário que a soma seja 7 ou 11.
            Se a soma for 4,5,6,8,9 ou 10 ganha um ponto, e se a soma se repetir no próximo lançamento você ganha o jogo
            Você perde se a soma for 2,3 ou 12 ou se você tiver um ponto e a soma do lançamento seguinte for 7 '''

#importa a biblioteca random para gerar números aleatórios
import random

resanterior = 0
cont = 0

#joga os dados, definindo valores aleatórios para eles e somando esses valores
def dados():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return d1+d2
def resultado(n1,n2):
    return n1==n2

#laço de repetição para jogar o jogo     
while True:
    comand = int(input('Digite 1 pra jogar ou 0 pra sair: '))
    
    if comand == 1:
        res = dados()
        print(res)
        
        if resultado(res,resanterior) == True:
            print('Você ganhou!')
            break
    
        elif cont>=1 and res==7:
            print('Você perdeu!')
            break
            
        elif res==7 or res==11:
            print('Você é um natural, Parabéns')
            resanterior = 0
            cont = 0
            break
        
        elif res==2 or res==3 or res==12:
            print('Craps!Você perdeu')
            resanterior = 0
            cont = 0
            break
        
        elif res==4 or res==5 or res==6 or res==8 or res==9 or res==10:
            resanterior = res
            cont+=1
            print('Você fez um ponto, faça mais um para ganhar')
    elif comand == 0:
        print('Obrigado por jogar!')
        break
    else:
        print('Comando inválido')


    