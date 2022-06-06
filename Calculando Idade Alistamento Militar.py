import datetime
sexo = int(input('Informe seu sexo sendo [1] para masculino e [2] para feminino: '))
if sexo != 1 and sexo !=2:
    print('Opção inválida. Digite novamente.')
elif sexo == 2:
        print('Você não precisa se alistar por ser do gênero FEMININO.')
elif sexo ==1:
    nasc = int(input('Digite seu ano de nascimento: '))
    ano = datetime.datetime.today().year
    idade = ano - nasc
    idaderest = abs(18 - idade)

    print('Você nasceu em {} e tem {} no ano de {}.'.format(nasc, idade, ano))
    if sexo == 1 and idade > 18:
        print('Você tem {} anos. Já se passaram {} da idade do alistamento.'.format(idade, idaderest))
    elif sexo == 1 and idade == 18:
        print('Você tem {} anos. Entre em contato com o exército para agendar seu alistamento.'.format(idade))
    elif sexo == 1 and idade < 18 and idaderest != 1:
        print('Você ainda não está na idade do alistamento. Faltam {} anos.'.format(idaderest))
    elif sexo == 1 and idade < 18 and idaderest == 1:
        print('Você ainda não está na idade do alistamento. Falta {} ano.'.format(idaderest))
