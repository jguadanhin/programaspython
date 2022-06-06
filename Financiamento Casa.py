vcasa = int(input('Qual o valor da casa? R$'))
salario = int(input('Qual o seu salário? R$'))
meses = int(input('Em quantos meses deseja pagar o financiamento? '))
prestacao = vcasa/meses

if prestacao <= salario*(30/100):
    print('Empréstimo aprovado! O valor mensal será de R${:.2f} e você pagará em {} meses.'.format(prestacao,meses))
elif prestacao >= salario*(30/100):
    print('Empréstimo negado! O valor da prestação é superior a 30% do seu salário.')
print(prestacao, meses, salario, vcasa)