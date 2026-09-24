"""

Desenvolva um algoritmo que peça números inteiros ao usuário até que o valor 0 (zero) seja digitado. 
O programa deve identificar e exibir qual foi o maior número negativo informado durante a execução.

"""

def main():
    num = int(0)
    maior = int(0)
    primeiro = True

    num = int(input())

    while(num != 0):
        if(num < 0):
            if(primeiro):
                maior = num
                primeiro = False
            elif(num > maior):
                maior = num

        num = int(input())

    if(primeiro):
        print(f'-1')
    else:
        print(f'{maior}')

    return 0

if __name__ == "__main__":
    main()