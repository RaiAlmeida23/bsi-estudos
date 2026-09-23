"""

Escreva um programa que leia o valor de uma compra e aplique um desconto progressivo conforme o valor. As regras de desconto são:

Compras até R$ 100,00: 5% de desconto.
Compras de R$ 101,00 até R$ 500,00: 10% de desconto.
Compras acima de R$ 500,00: 15% de desconto.

"""

def main():
    valor = int(0)
    
    desconto = float(0)
    final = float(0)
    
    valor = int(input())

    if(valor <= 100):
        desconto = valor * 0.05
        
    elif(valor >= 101 and valor <= 500):
        desconto = valor * 0.10
        
    elif(valor >= 500):
        desconto = valor * 0.15
    
    final = valor - desconto
    print(f'Valor final com desconto: R$ {final:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()