"""

Desenvolva um algoritmo que leia um número inteiro qualquer, extraia isoladamente os seus dois últimos algarismos (o das dezenas e o das unidades) e exiba a soma entre eles.

"""

def main():
    num = int(0)
    uni = int(0)
    dez = int(0)
    soma = int(0)
    
    num = int(input())
    
    uni = num % 10
    dez = (num // 10) % 10
    soma = uni + dez
    
    print(f'{soma}')
    
    return 0

if __name__ == "__main__":
    main()