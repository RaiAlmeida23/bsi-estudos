"""

Desenvolva um algoritmo que solicite ao usuário um número inteiro inicial. 
Em seguida, peça a quantidade de números que serão somados a este valor inicial. 
O programa deve ler cada um desses números e, ao final, exibir o resultado da soma total.

"""

def main():
    num = int(0)
    qtd = int(0)
    soma = int(0)
    i = int(0)
    
    num = int(input())
    qtd = int(input())
    
    soma = num
    for i in range(qtd):
        num = int(input())
        soma = soma + num
        i = i + 1
    
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()