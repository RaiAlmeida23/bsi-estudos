"""

Faça um programa que leia dois números inteiros, a e b. 
Se a for maior que b, apresente a soma dos dois; caso a seja menor ou igual a b, apresente o resultado da multiplicação dos dois. 
Considere que não serão informados números iguais.

"""

def main():
    a = int(0)
    a = int(0)
    soma = int(0)
    mult = int(0)
    
    a = int(input())
    b = int(input())
    
    soma = a + b
    mult = a * b
    
    if(a > b):
        print(f'{a} + {b} = {soma}')
        
    else:
         print(f'{a} x {b} = {mult}')
    
    return 0

if __name__ == "__main__":
    main()