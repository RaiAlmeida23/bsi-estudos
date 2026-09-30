"""

Desenvolva um algoritmo que leia 5 valores inteiros fornecidos pelo usuário. 
Após a leitura de todos os números, o programa deve calcular e imprimir a soma total desses valores.

"""

def main():
    num = int(0)
    soma = int(0)
    i = int(0)
    
    for i in range(1, 6, 1):
        num = int(input())
        soma = soma + num
    
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()