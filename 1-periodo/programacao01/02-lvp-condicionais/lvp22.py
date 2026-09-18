"""

Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. 
Calcular e escrever a quantidade média (quantidade média = (quantidade máxima + quantidade mínima) / 2). Se a quantidade em estoque 
for maior ou igual a quantidade média escrever a mensagem NÃO EFETUAR COMPRA, senão escrever a mensagem EFETUAR COMPRA.

Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    estoque = int(0)
    maxima = int(0)
    minima = int(0)
    
    media = float(0)
    
    estoque = int(input())
    maxima = int(input())
    minima = int(input())
    
    media = (maxima + minima) / 2
    
    if(estoque >= media):
        print(f'NÃO EFETUAR COMPRA')
        
    else:
        print(f'EFETUAR COMPRA')
    
    return 0
    
if __name__ == "__main__":
    main()