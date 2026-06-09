custo = int(input("Qual o valor do produto? "))
pagar = int(input(
    '''FORMAS DE PAGAMENTO
[1] Pagamento a vista dinheiro
[2] Pagamento a vista no cartão
[3] 2x no cartão
[4] 3x no cartão
Qual das oções o cliente prefere? '''))
if pagar == 1:
    dinheiro = custo - (custo * 10/100)
    print(f"Sua compra foi de R${custo:.2f} e vai custar R${dinheiro:.2f}")
elif pagar == 2:
    cartao = custo - (custo * 5 / 100)
    print(f"Sua compra foi de R${custo:.2f} e vai custar R${cartao:.2f}")
elif pagar == 3:
    parcela2x = custo / 2
    print(
        f"Sua compra foi de R${custo:.2f} parcelado em 2x de R${parcela2x:.2f}")
elif pagar == 4:
    parcelas = int(input("Quantas parcelas?"))
    juros = (custo * 20 / 100) + custo
    div = juros / parcelas
    print(
        f"Foi parcelado em {parcelas}x de R${div:.2f}\nO produto no valor de R${custo:.2f} vai custar R${juros:.2f} no final")
