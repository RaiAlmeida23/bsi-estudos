"""

Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos dois maiores valores.

"""

def main():
    n1 = int(0)
    n2 = int(0)
    n3 = int(0)
    soma = float(0)
    maior1 = int(0)
    maior2 = int(0)
    
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    if (n1 > n2 and n1 > n3):
        if(n2 > n3):
            maior1 = n1
            maior2 = n2
        else:
            maior1 = n1
            maior2 = n3
    
    elif (n2 > n3 and n2 > n1):
        if(n3 > n1):
            maior1 = n2
            maior2 = n3
        else:
            maior1 = n2
            maior2 = n1
            
    elif (n3 > n1 and n3 > n2):
        if(n1 > n2):
            maior1 = n3
            maior2 = n1
        else:
            maior1 = n3
            maior2 = n2
    
    soma = maior1 + maior2
    print(f'{soma:.1f}')
    
    return 0

if __name__ == "__main__":
    main()