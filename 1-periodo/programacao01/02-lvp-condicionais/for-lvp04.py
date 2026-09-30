"""

Desenvolva um algoritmo que leia um valor inteiro N e imprima todos os valores inteiros entre 1 e N (ambos inclusive). 
Considere que N será sempre maior que zero.

"""

def main():
    num = int(0)
    i = int(0)
    
    num = int(input())
    
    for i in range(1, num + 1, 1):
        print(f'{i}')
    
    return 0
    
if __name__ == "__main__":
    main()