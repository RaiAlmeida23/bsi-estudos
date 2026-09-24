"""

Desenvolva um algoritmo que solicite ao usuário uma sequência de números inteiros. 
O programa deve identificar e exibir o maior número da lista. A entrada de dados deve ser encerrada quando o usuário digitar o valor 0 (zero).

"""

def main():
    num = int(0)
    maior = int(0)
    
    primeiro = True
    
    num = int(input())
    
    while(num != 0):

        if(primeiro == True):
            maior = num
            primeiro = False

        elif(num > maior):
            maior = num

        num = int(input())
    
    print(f'{maior}')
    
    return 0
    
if __name__ == "__main__":
    main()