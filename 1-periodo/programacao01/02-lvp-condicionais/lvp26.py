"""

Dados, como entrada, quatro valores do tipo inteiro, faça um programa, em Python 3.x, que efetue a soma dos TRÊS MENORES valores informados.

"""

def main():
    num1 = int(0)
    num2 = int(0)
    num3 = int(0)
    num4 = int(0)
    soma = int(0)
    
    num1 = int(input()) 
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    
    if (num1 > num2 and num1 > num3 and num1 > num4):
        soma = num2 + num3 + num4
    
    elif (num2 > num3 and num2 > num4 and num2 > num1):
        soma = num1 + num3 + num4
    
    elif (num3 > num4 and num3 > num1 and num3 > num2):
        soma = num1 + num2 + num4
    
    elif (num4 > num1 and num4 > num2 and num4 > num3):
        soma = num1 + num2 + num3

    print(f'{soma}')
    
    return 0

if __name__ == "__main__":
    main()