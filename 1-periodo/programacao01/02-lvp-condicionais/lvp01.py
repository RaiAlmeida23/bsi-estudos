"""

Faça um programa que leia um número inteiro e diga se ele é par ou ímpar.

"""

def main():
    num = int(0)
    
    num = int(input())
    
    if(num % 2 == 0):
        print(f'{num} é PAR')
        
    else:
         print(f'{num} é ÍMPAR')
    
    return 0

if __name__ == "__main__":
    main()