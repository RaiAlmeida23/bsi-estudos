"""

Desenvolva um algoritmo que solicite números inteiros até que o valor -1 seja digitado. 
O programa deve identificar e exibir o menor número par da sequência. 
Caso nenhum número par seja informado, a saída deve ser -1.

"""

def main():
    num = int(0)
    menor = int(0)
    primeiro = True

    num = int(input())

    while(num != -1):
        if(num % 2 == 0):
            if(primeiro):
                menor = num
                primeiro = False
            elif(num < menor):
                menor = num

        num = int(input())

    if(primeiro):
        print(f'-1')
    else:
        print(f'{menor}')

    return 0

if __name__ == "__main__":
    main()