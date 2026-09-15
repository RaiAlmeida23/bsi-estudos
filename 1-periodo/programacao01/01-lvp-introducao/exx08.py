"""
Desenvolva um programa que receba um número inteiro como entrada. 
O algoritmo deve ser capaz de identificar e exibir apenas o algarismo que ocupa a casa das dezenas do número fornecido.

"""

def main():
    num = int(0)
    dez = int(0)
    
    num = int(input())
    
    dez = (num // 10) % 10
    
    print(f'{dez}')
    
    return 0
    
if __name__ == "__main__":
    main()