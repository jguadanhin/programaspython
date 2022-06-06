from random import randint
from time import sleep
nm = randint(1,3)
print('Escolha: \n1 - Pedra\n2 - Papel\n3 - Tesoura')
np = int(input('Digite sua opção: '))
if nm == 1:
    maquina = 'pedra'
elif nm == 2:
    maquina = 'papel'
elif nm ==3:
    maquina = 'tesoura'
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador escolheu {}.'.format(maquina))
if nm == 1 and np == 1 or nm == 2 and np == 2 or nm == 3 or np == 3:
    print('Empate!')
elif nm == 1 and np == 2:
    print('Você venceu!')
elif nm == 1 and np ==3:
    print('Você perdeu!')
elif nm == 2 and np ==1:
    print('Você perdeu!')
elif nm == 2 and np ==3:
    print('Você venceu!')
elif nm == 3 and np==1:
    print('Você perdeu!')
elif nm == 3 and np ==2:
    print('Você ganhou!')