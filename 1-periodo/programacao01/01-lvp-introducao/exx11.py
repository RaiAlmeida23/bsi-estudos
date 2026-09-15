"""

Desenvolva um algoritmo que leia um número inteiro qualquer e exiba na tela apenas o dígito correspondente à casa das centenas.

"""

def main():
    num = int(0)
    cen = int(0)
    
    num = int(input())
    
    cen = (num // 100) % 10
    
    print(f'{cen}')
    
    return 0
    
if __name__ == "__main__":
    main()