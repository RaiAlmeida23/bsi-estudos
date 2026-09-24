"""

Desenvolva um algoritmo que solicite números inteiros ao usuário até que o valor 999 seja digitado. 
O programa deve calcular a média aritmética apenas dos números pares informados. 
Caso nenhum número par seja inserido, a saída deve ser -1.

"""

def main():
    num = int(0)
    contP = int(0)
    soma = int(0)
    meadia = int(0)
    
    num = int(input())
    while(num != 999):
        if(num % 2 == 0):
            soma = soma + num
            contP = contP + 1
        num = int(input())
    
    if(contP == 0):
        print(f'-1')
        
    else:    
        media = soma / contP
        print(f'{media:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()