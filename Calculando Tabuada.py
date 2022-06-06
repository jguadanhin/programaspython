numero = int(input('Digite um número: '))
print('A tabuada de {} é:'.format(numero))
for c in range(1,11):
    print('{} * {:=2} = {:=2}'.format(numero, c, numero*c))