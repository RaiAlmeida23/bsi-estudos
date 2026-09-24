"""

Desenvolva um algoritmo que solicite ao usuário uma sequência de números inteiros. 
O programa deve contar quantos desses números são pares. 
A entrada de dados deve ser encerrada quando o usuário digitar o valor -1.

"""

def main():
    num = int(0)
    par = int(0)
    
    while(num != -1):
        num = int(input())
        if(num % 2 == 0):
            par = par + 1
            
    print(f'{par}')
    
    return 0
    
if __name__ == "__main__":
    main()