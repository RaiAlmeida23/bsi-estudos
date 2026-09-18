"""

Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as idades dos homens serão sempre diferentes entre si, 
bem como as das mulheres). Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades do homem 
mais novo com a mulher mais velha.

Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    h1 = int(0)
    h2 = int(0)
    m1 = int(0)
    m2 = int(0)
    
    som = int(0)
    pro = int(0)
    
    h1 = int(input())
    h2 = int(input())
    m1 = int(input())
    m2 = int(input())
    
    if(h1 > h2):
        if(m1 < m2):
            som = h1 + m1
            pro = h2 * m2
        else:
            som = h1 + m2
            pro = h2 * m1
            
    else:
        if(m1 < m2):
            som = h2 + m1
            pro = h1 * m2
        else:
            som = h2 + m2
            pro = h1 * m1
            
    print(f'{som} {pro}')
    
    return 0
    
if __name__ == "__main__":
    main()