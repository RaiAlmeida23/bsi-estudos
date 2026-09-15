"""

Desenvolva um programa que solicite ao usuário dois números inteiros: o primeiro representando a base e o segundo representando o expoente. 
O algoritmo deve calcular o valor da base elevada ao expoente fornecido e exibir o resultado final.

"""

def main():
    base = int(0)
    expo = int(0)
    result = int(0)
    
    base = int(input())
    expo = int(input())
    
    result = base ** expo
    
    print(f'{result}')
    
    return 0
    
if __name__ == "__main__":
    main()