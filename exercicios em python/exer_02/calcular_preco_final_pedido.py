valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

precoHamburguer = valorHamburguer * quantidadeHamburguer
precoBebida = valorBebida * quantidadeBebida
precoTotal = precoHamburguer + precoBebida
troco = valorPago - precoTotal

mensagem = f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}."
print(mensagem)