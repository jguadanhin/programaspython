pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(pt,pt+(razao*10), razao):
    print(c,end=' > ')
print('Acabou!')
