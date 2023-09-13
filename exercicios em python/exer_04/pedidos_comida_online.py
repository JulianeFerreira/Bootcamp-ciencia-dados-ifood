def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
 
    cupom_desconto = input()
  
    if cupom_desconto == "10%":
        total = total * 0.9
    elif cupom_desconto == "20%":
        total = total * 0.8
    
    print(f"Valor total: {total:.2f}")
 
 
if __name__ == "__main__":
    main()