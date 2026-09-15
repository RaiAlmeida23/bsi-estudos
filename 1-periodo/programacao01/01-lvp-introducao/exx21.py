"""

Desenvolva um algoritmo que leia o valor do raio de uma circunferência. 
O programa deve calcular a área correspondente utilizando a fórmula clássica A=π⋅r2, adotando estritamente 
o valor de 3.14159 para a constante π.

"""

def main():
    raio = int(0)
    area = float(0.0)
    
    raio = int(input())
    
    area = 3.14159 * (raio ** 2)
    
    print(f'Área={area:.5f}')
    
    return 0
    
if __name__ == "__main__":
    main()