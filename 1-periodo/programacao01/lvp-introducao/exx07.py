"""
Desenvolva um programa que receba como entrada um número inteiro de qualquer magnitude. 
O algoritmo deve processar esse valor para identificar e exibir exclusivamente o seu último dígito (o algarismo das unidades).

"""

def main():
    num = int(0)
    uni = int(0)
    
    num = int(input())
    
    uni = num % 10
    
    print(f'{uni}')
    
    return 0
    
if __name__ == "__main__":
    main()