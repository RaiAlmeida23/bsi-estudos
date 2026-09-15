"""

Desenvolva um algoritmo que leia um número inteiro de exatamente 3 dígitos e o armazene na variável n. 
O programa deve calcular o valor correspondente a esse número escrito de trás para frente e guardá-lo em uma única variável chamada inverso.

"""

def main():
    num = int(0)
    
    uni = int(0)
    dez = int(0)
    cen = int(0)
    inverso = int(0)
    
    num = int(input())
    
    uni = num % 10
    dez = (num // 10) % 10
    cen = (num // 100) % 10
    inverso = (uni * 100) + (dez * 10) + cen
    
    print(f'O inverso de {num} é {inverso}.')
    
    return 0
    
if __name__ == "__main__":
    main()