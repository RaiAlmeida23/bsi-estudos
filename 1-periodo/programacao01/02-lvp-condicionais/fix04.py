"""

Escreva um programa que leia um número inteiro e determine se ele é múltiplo de 3, múltiplo de 5, de ambos, ou de nenhum dos dois.

"""

def main():
    num = int(0)
    
    num = int(input())
    
    if(num % 3 == 0):
        if(num % 5 == 0):
            print(f'Múltiplo de 3 e 5')
            
        else:
            print(f'Múltiplo de 3')
            
    elif(num % 5 == 0):
        print(f'Múltiplo de 5')
    
    else:
        print(f'Não é múltiplo de 3 nem de 5')
        
    return 0
    
if __name__ == "__main__":
    main()