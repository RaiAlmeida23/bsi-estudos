"""

Escreva um algoritmo que realize a leitura de um valor inteiro N. 
O programa deve imprimir todos os valores inteiros situados no intervalo entre 1 (inclusive) e N (inclusive). 
Considere que, para este exercício, o valor de N fornecido pelo usuário será sempre maior que zero.

"""

def main():
    n = int(0)
    i = int(0)
    
    n = int(input())
    
    i = 1
    while(i <= n):
        print(f'{i}')
        i = i + 1
    
    return 0
    
if __name__ == "__main__":
    main()