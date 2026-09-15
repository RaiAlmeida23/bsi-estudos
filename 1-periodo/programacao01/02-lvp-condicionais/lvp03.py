"""

Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.

"""

def main():
    a = int(0)
    b = int(0)
    maior = int(0)
    menor = int(0)
    diff = int(0)
    
    a = int(input())
    b = int(input())
    
    if(a > b):
        maior = a
        menor = b
        
    else:
        maior = b
        menor = a
    
    diff = maior - menor
    print(f'{maior} - {menor} = {diff}')
    
    return 0

if __name__ == "__main__":
    main()