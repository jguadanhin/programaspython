nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media >= 7:
    print('Parabéns! Sua média foi {:.1f} e você está aprovado.'.format(media))
elif media < 5:
    print('Você está reprovado pois sua média foi {:.1f}.'.format(media))
else:
    print('Você está na recuperação! Pois sua média foi {:.1f}.'.format(media))
