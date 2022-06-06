pt = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
print('A progressão aritmética de {} com a razão {} é: '.format(pt, razao, end =''))
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('Acabou!')
    mais = int(input('Quantos termos adicionais você gostaria de visualizar?'))
print('Acabou novamente!')
