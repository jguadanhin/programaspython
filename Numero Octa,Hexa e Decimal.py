import math
num = int(input('Digite um numero: '))
print('Selecione uma das opções abaixo:')
print('[1] para BINÁRIO.')
print('[2] para OCTAL.')
print('[3] para HEXADECIMAL.')
escolha = int(input('Selecione a opção acima: '))
if escolha == 1:
    print('O número {} convertido em BINÁRIO é {}.'.format(num, bin(num)))
elif escolha ==2:
    print('O número {} convertido em OCTAL é {}.'.format(num, oct(num)))
elif escolha ==3:
    print('O número {} convertido em HEXADECIMAL é {}.'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente!')