"""

Desenvolva um algoritmo que utilize uma estrutura de repetição para exibir na tela os números inteiros de 10 até 0, em ordem decrescente. 
Cada número deve ser apresentado em uma linha exclusiva.

"""

def main():
    i = int(0)
    
    i = 10
    
    while(i >= 0):
        print(f'{i}')
        i = i - 1
    
    return 0
    
if __name__ == "__main__":
    main()