"""

Faça um programa que receba três valores inteiros (a, b e c) e calcule a soma de a e b multiplicada pelo valor de c, aplicando a relação:
Formatação da Saída: A saída deve apresentar a estrutura completa da equação armada e o resultado final no formato (a + b) x c = resultado.

"""

def main():
    a = int(0)
    b = int(0)
    c = int(0)
    resultado = int(0)
    
    a = int(input())
    b = int(input())
    c = int(input())
    
    resultado = (a + b) * c
    
    print(f'({a} + {b}) x {c} = {resultado}')
    
    return 0
    
if __name__ == "__main__":
    main()