altura = float(input('Digite sua altura em metros (exemplo: 1.85): '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura*2)
if imc < 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do peso ideal.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.2f}. Você está no seu peso ideal.'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é {:.2f}. Voce está com sobrepeso.'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {:.2f}. Você está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}. Você está com obesidade mórbida.'.format(imc))
