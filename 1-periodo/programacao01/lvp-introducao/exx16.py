"""

Desenvolva um algoritmo que leia um número inteiro de 3 dígitos. 
O programa deve isolar cada algarismo e exibir o produto (multiplicação) entre eles.

"""

def main():
    num = int(0)
    
    uni = int(0)
    dez = int(0)
    cen = int(0)
    prod = int(0)
    
    num = int(input())
    
    uni = num % 10
    dez = (num // 10) % 10
    cen = (num // 100) % 10
    prod = uni * dez * cen
    
    print(f'{prod}')
    
    return 0
    
if __name__ == "__main__":
    main()