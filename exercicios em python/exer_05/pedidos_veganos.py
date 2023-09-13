numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False

    opcao_vegano = input()
    if opcao_vegano == "s":
        ehVegano = True

    if ehVegano:
        tipo_vegano = "Vegano"
    else:
        tipo_vegano = "Nao-vegano"

    print(f"Pedido {i}: {prato} ({tipo_vegano}) - {calorias} calorias")