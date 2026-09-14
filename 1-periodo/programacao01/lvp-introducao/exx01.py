# Desenvolva um programa que seja capaz de realizar a leitura de dois números inteiros fornecidos pelo usuário
# Após a leitura, o sistema deve calcular a soma entre esses valores e exibir o resultado final

def main():
    num1 = int(0)
    num2 = int(0)
    soma = int(0)
    
    num1 = int(input())
    num2 = int(input())
    
    soma = num1 + num2
    
    print(f'{soma}')
    return 0

if __name__ == "__main__":
    main()
