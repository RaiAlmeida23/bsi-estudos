"""

Escreva um programa que realize a leitura de 5 números inteiros. 
O algoritmo deve processar essas entradas para calcular dois indicadores distintos: a soma total de todos os 
números positivos informados e a média aritmética de todos os números negativos digitados.

"""

def main():
    i = int(0)
    n = int(0)
    somap = int(0)
    soman = int(0)
    contn = int(0)
    
    i = 0
    while(i < 5):
        n = int(input())
        if(n < 0):
            soman = soman + n
            contn = contn + 1
            
        else:
            somap = somap + n
            
        i = i + 1
        
    print(f'{somap}')
    
    if(contn > 0):
        print(f'{soman/contn:.0f}')
        
    return 0

if __name__ == "__main__":
    main()