"""

Desenvolva um algoritmo que leia um número inteiro qualquer, extraia isoladamente os seus três últimos algarismos (centena, dezena e unidade) e exiba o resultado da soma entre eles.

"""

def main():
    num = int(0)
    
    uni = int(0)
    dez = int(0)
    cen = int(0)
    soma = int(0)
    
    num = int(input())
    
    uni = num % 10
    dez = (num // 10) % 10
    cen = (num // 100) % 10
    soma = uni + dez + cen
    
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()