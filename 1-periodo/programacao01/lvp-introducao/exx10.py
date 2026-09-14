"""

Escreva um programa que realize a leitura de um número inteiro. 
O algoritmo deve calcular a raiz quadrada desse valor e apresentar o resultado na tela, garantindo que a exibição contenha exatamente duas casas decimais.

"""

def main():
    num = int(0)
    result = float(0.0)
    
    num = int(input())
    
    result = num ** (0.5)
    
    print(f'{result:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()