"""

Faça um programa que receba dois números pelo teclado, efetue a soma entre eles e, em seguida, calcule e apresente a raiz quadrada desse resultado.
Formatação da Saída: O valor resultante deve ser apresentado obrigatoriamente formatado com 3 casas decimais.

"""

def main():
    num1 = int(0)
    num2 = int(0)
    resultado = float(0.0)
    
    num1 = int(input())
    num2 = int(input())
    
    resultado = (num1 + num2) ** 0.5
    
    print(f'{resultado:.3f}')
    
    return 0
    
if __name__ == "__main__":
    main()