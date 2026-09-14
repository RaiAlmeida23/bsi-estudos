"""

Desenvolva um algoritmo que leia dois números inteiros (fornecidos um em cada linha). 
O programa deve calcular a soma entre esses dois números e, em seguida, exibir o valor dessa soma elevado ao quadrado.

"""

def main():
    num1 = int(0)
    num2 = int(0)
    soma = int(0)
    quad = int(0)
    
    num1 = int(input())
    num2 = int(input())
    
    soma = num1 + num2
    quad = soma ** 2
    
    print(f'{quad}')
    
    return 0
    
if __name__ == "__main__":
    main()