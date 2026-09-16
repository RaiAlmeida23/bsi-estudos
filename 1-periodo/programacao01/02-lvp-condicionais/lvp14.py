"""

Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.
Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    n1 = int(0)
    n2 = int(0)
    n3 = int(0)
    maior = int(0)
    
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    if(n1 > n2 and n1 > n3):
        maior = n1
        
    elif(n2 > n3 and n2 > n1):
        maior = n2
    
    elif(n3 > n1 and n3 > n2):
        maior = n3
    
    print(f'{maior}')
    
    return 0
    
if __name__ == "__main__":
    main()