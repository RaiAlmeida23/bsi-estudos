"""

Desenvolva um algoritmo que leia o custo de fábrica de um carro novo. 
O programa deve aplicar uma taxa de 28% do distribuidor e 45% de impostos (ambos calculados sobre o custo de fábrica) para descobrir e exibir o custo final ao consumidor.

"""

def main():
    custo = float(0.0)
    
    distribuidor = float(0.0)
    impostos = float(0.0)
    total = float(0.0)
    
    custo = float(input())
    
    distribuidor = (custo * 28) // 100
    impostos = (custo * 45) // 100
    total = round((custo + distribuidor + impostos), 1)
    
    print(f'{total}')
    
    return 0
    
if __name__ == "__main__":
    main()