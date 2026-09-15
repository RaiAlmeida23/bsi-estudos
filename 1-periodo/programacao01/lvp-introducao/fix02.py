"""

Faça um programa que receba dois números inteiros, calcule a diferença entre o primeiro e o segundo número, eleve 
o resultado dessa subtração ao quadrado e, por fim, apresente o valor obtido.

"""

def main():
    num1 = float(0.0)
    num2 = float(0.0)
    resultado = float(0.0)
    
    num1 = float(input())
    num2 = float(input())
    
    resultado = (num1 - num2) ** 2
    
    print(f'{resultado:.0f}')
    
    return 0
    
if __name__ == "__main__":
    main()