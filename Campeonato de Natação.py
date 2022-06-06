import datetime
ano = datetime.datetime.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = ano-nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você se enquadra na categoria MIRIM de natação.')
elif idade <=14:
    print('Você se enquadra na categoria INFANTIL de natação.')
elif idade <19:
    print('Você se encontra na categoria JUNIOR de natação.')
elif idade <= 25:
    print('Você se encontra na categoria SÊNIOR de natação.')
elif idade >25:
    print('Você se encontra na categoria MASTER de natação.')

