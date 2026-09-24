"""

Desenvolva um algoritmo que solicite uma sequência de números inteiros ao usuário. 
O programa deve calcular e exibir a soma apenas dos números ímpares. 
A entrada de dados deve ser encerrada quando o usuário digitar o valor 0 (zero).

"""

def main():
    num = int(0)
    soma = int(0)
    
    num = int(input())
    while(num != 0):
        if(num % 2 != 0):
            soma = soma + num
        num = int(input())
            
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()