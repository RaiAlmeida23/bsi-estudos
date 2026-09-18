"""

Utilizando, apenas e obrigatoriamente, ESTRUTURAS CONDICIONAIS, faça um programa, em Python 3.x, que receba como entrada de dados, via teclado, 
4 valores INTEIROS (considere que não serão informados valores iguais) e apresente, como saída de dados, a soma do MAIOR valor com o MENOR valor.

"""

def main():
    
    num1 = int(0)
    num2 = int(0)
    num3 = int(0)
    num4 = int(0)
    
    maior = int(0)
    menor = int(0)
    soma = int(0)
    
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    
    if (num1 < num2 and num1 < num3 and num1 < num4):
        menor = num1
        if(num2 > num3 and num2 > num4):
            maior = num2
        
        elif(num3 > num4 and num3 > num2):
            maior = num3
        
        else:
            maior = num4
            
    elif (num2 < num3 and num2 < num4 and num2 < num1):
        menor = num2
        if(num3 > num4 and num3 > num1):
            maior = num3
        
        elif(num4 > num1 and num4 > num3):
            maior = num4
        
        else:
            maior = num1
            
    elif (num3 < num4 and num3 < num1 and num3 < num2):
        menor = num3
        if(num4 > num1 and num4 > num2):
            maior = num4
        
        elif(num1 > num2 and num1 > num4):
            maior = num1
        
        else:
            maior = num2
    
    elif (num4 < num1 and num4 < num2 and num4 < num3):
        menor = num4
        if(num1 > num2 and num1 > num3):
            maior = num1
        
        elif(num2 > num3 and num2 > num1):
            maior = num2
        
        else:
            maior = num3
    
        
    soma = menor + maior
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()