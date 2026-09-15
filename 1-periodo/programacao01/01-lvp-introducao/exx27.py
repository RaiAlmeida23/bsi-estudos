"""

Desenvolva um algoritmo que leia a massa (m) de um corpo em quilogramas (Kg) e a força 
resultante (F) em Newtons (N), inseridas uma por linha. 
O programa deve calcular a aceleração (a) adquirida pelo corpo, realizando o arranjo da fórmula original:

F=m⋅a
Para isolar e encontrar o valor da aceleração, utilize a derivação matemática:

a=F/m

"""

def main():
    m = float(0.0)
    f = float(0.0)
    a = float(0.0)
    
    m = float(input())
    f = float(input())
    
    a = f / m
    
    print(f'{a:.1f}')
    
    return 0
    
if __name__ == "__main__":
    main()