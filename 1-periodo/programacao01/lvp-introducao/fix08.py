"""

Faça um programa que receba três números (n1, n2 e n3) e, em seguida, seus respectivos pesos (p1, p2 e p3). 
O programa deve calcular a média ponderada através da fórmula:

Formatação da Saída: A saída deve exibir a equação armada com os valores e a soma dos pesos no formato (n1 x p1 + n2 x p2 + n3 x p3) / soma_pesos = media, 
formatando a média final obrigatoriamente com duas casas decimais.

"""

def main():
    n1 = int(0)
    n2 = int(0)
    n3 = int(0)
    p1 = int(0)
    p2 = int(0)
    p3 = int(0)
    
    pesos = int(0)
    soma = float(0.0)
    
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())
    
    pesos = p1 + p2 + p3
    soma = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / pesos
    
    print(f'({n1} x {p1} + {n2} x {p2} + {n3} x {p3}) / {pesos} = {soma:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()