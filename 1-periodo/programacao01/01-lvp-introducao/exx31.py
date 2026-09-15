"""

Desenvolva um algoritmo que leia o tamanho em metros quadrados (m2) da área a ser pintada. 
Sabendo que a cobertura da tinta é de 1 litro para cada 6 m2, o programa deve calcular a litragem 
total necessária e simular duas situações independentes de compra comerciais:

Situação 1: Comprar apenas latas de 18 litros (Custo: R$ 80,00 cada).
Situação 2: Comprar apenas galões de 3,6 litros (Custo: R$ 25,00 cada).

"""

import math

def main():
    area = float(0)
    litros = float(0)
    latas = int(0)
    galoes = int(0)
    precoL = float(0)
    precoG = float(0)
    
    area = float(input())
    
    litros = area / 6
    latas = math.ceil(litros / 18)
    precoL = latas * 80
    galoes = math.ceil(litros / 3.6)
    precoG = galoes * 25
    
    print(f'Você utilizará {latas} latas de 18L. Valor = {precoL:.2f}\nVocê utilizará {galoes} galões de 3.6L. Valor = {precoG:.2f}')
    
    return 0

if __name__ == "__main__":
    main()