"""

Escreva um algoritmo que realize a leitura de 5 valores inteiros fornecidos pelo usuário. 
O programa deve processar essas entradas de forma iterativa, somando cada novo valor ao total acumulado, e exibir o resultado final da soma ao término das leituras.

"""

def main():
    valor = int(0)
    soma = int(0)
    i = int(0)
    
    i = 1
    while(i <= 5):
        valor = int(input())
        soma = soma + valor
        i = i + 1
    
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()