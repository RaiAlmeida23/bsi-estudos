# Escreva um programa que realize a leitura de dois números inteiros. 
# O algoritmo deve calcular o resultado da multiplicação entre o primeiro e o segundo número e, em seguida, apresentar o valor total na saída de dados.

def main():
    num1 = int(0)
    num2 = int(0)
    produto = int(0)
    
    num1 = int(input())
    num2 = int(input())
    
    produto = num1 * num2
    
    print(f'{produto}')
    
    return 0
    
if __name__ == "__main__":
    main()
