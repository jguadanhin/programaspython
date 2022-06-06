pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Media'] = float(input('Média: '))
if pessoa['Media'] >= 7:
    pessoa['Situação'] = 'Aprovado'
else:
    pessoa['Situação'] = 'Reprovado'
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')
