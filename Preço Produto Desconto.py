preco = float(input('Digite o valor do produto: R$'))
print('Para pagamento à vista no dinheiro ou cheque com 10% de desconto digite 1')
print('Para pagamento à vista no cartão com 5% de desconto digite 2')
print('Para pagamento parcelado em até 2x no cartão digite 3')
print('Para pagamento parcelado em 3x ou mais no cartão digite 4')
pagamento = int(input('Informe a condição de pagamento: '))
if pagamento == 1:
    print('O valor a ser pago é de R${:.2f}.'.format(preco-(preco*(10/100))))
elif pagamento ==2:
    print('O valor a ser pago é de R${:.2f}.'.format(preco-(preco*(5/100))))
elif pagamento ==3:
    print('O valor a ser pago é de R${:.2f}. Podendo ser parcelado em 2x de {:.2f}.'.format(preco, preco/2))
elif pagamento ==4:
    meses = int(input('Digite o número de vezes que deseja parcelar sua compra:'))
    print('O valor a ser pago é de R${:.2f} com parcelas de R${:.2f}.'.format(preco+(preco*(20/100)), preco/meses))