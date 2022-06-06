cont = soma = maior = menor = 0
step = ''
while step != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    step = str(input('Você deseja continuar? [S/N]: ')).strip().upper()
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
print('A soma dos valores é {}.'.format(soma))
print('A média dos valores é {}.'.format(soma/cont))
