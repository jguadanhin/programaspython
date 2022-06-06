from random import randint
computador = randint(1, 10)
tentativa = 0
pessoa = False
while not pessoa:
    num = int(input('Tente adivinhar um número entre 0 e 10: '))
    tentativa += 1
    if num == computador:
        pessoa = True
    else:
        if num > computador:
            print('Menos... tente novamente um número: ')
        elif computador > num:
            print('Mais... tente novamente um número: ')
print('Parabéns! Você acertou o número que a máquina pensou. Porém você precisou de {} tentativas para acertar.'.format(tentativa))
