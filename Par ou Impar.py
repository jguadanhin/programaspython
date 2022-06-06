from random import randint
cont = 0
while True:
    num = int(input('Digite um valor: '))
    poi = str(input('Você quer PAR ou ÍMPAR [P/I]: ')).strip().upper()
    computador = randint(0, 10)
    soma = computador + num
    if soma % 2 == 0 and poi in 'P':
        print(f'{soma} é PAR e você venceu.')
        cont += 1
    elif soma % 2 == 0 and poi in 'I':
        print(f'{soma} é PAR e você perdeu.')
        break
    elif soma % 2 != 0 and poi in 'P':
        print(f'{soma} é ÍMPAR e você perdeu.')
        break
    elif soma % 2 != 0 and poi in 'I':
        print(f'{soma} é ÍMPAR e você venceu.')
        cont += 1
if cont > 1:
    print(f'Você venceu {cont} vezes.')
if cont == 1:
    print(f'Você venceu {cont} vez.')
if cont == 0:
    print('Você não venceu nenhuma vez.')