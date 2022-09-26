import time

hora_atual = time.strftime('%H:%M:%S')
seg = int(time.mktime(time.localtime()))
minutos = int(seg/60)
horas = int(minutos/60)
dias = int(horas/24)
anos = int(dias/365)
print(f'Agora são {hora_atual}, se passaram {dias} dias desde 01/01/1970')