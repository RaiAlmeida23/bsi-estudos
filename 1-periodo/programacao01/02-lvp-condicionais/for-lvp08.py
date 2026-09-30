"""

Desenvolva um algoritmo que leia 5 valores inteiros. 
Ao final, apresente a soma apenas dos valores que forem positivos e a média aritmética apenas dos valores que forem negativos.

"""

def main():
    num = int(0)
    somaP = int(0)
    somaN = int(0)
    media = float(0.0)
    cont = int(0)
    i = int(0)
    
    for i in range(0, 5, 1):
        num = int(input())
        if(num < 0):
            somaN = somaN + num
            cont = cont + 1
        else:
            somaP = somaP + num
    
    if(cont > 0):
        media = somaN / cont
    else:
        media = 0.0
        
    print(f'{somaP}\n{media:.1f}')
    
    return 0
    
if __name__ == "__main__":
    main()