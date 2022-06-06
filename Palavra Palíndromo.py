frase = str(input('Digite a frase ou palavra desejada: ')).strip().upper()
if frase == frase[::-1]:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
print(frase[::-1])
