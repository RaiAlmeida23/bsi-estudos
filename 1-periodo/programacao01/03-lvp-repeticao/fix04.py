"""

Desenvolva um algoritmo que peça ao usuário uma quantidade total de números a serem lidos. 
Em seguida, o programa deve ler esses números e, ao final, exibir quantos deles eram negativos (menores que zero).

"""

def main():
    qtd = int(0)
    num = int(0)
    cont = int(0)
    contN = int(0)
    
    qtd = int(input())
    for cont in range(qtd):
        num = int(input())
        if(num < 0):
            contN = contN + 1
        
        cont = cont + 1
        
    print(f'{contN}')
    
    return 0

if __name__ == "__main__":
    main()