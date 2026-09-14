"""
Escreva um algoritmo que leia quatro valores inteiros: o número total de eleitores votantes de um município, 
seguido pela quantidade de votos brancos, votos nulos e votos válidos. O sistema deve calcular e exibir o 
percentual que cada categoria de voto representa em relação ao total de eleitores.

"""

def main():
    total = int(0)
    brancos = int(0)
    nulos = int(0)
    validos = int(0)
    
    pBrancos = float(0)
    pNulos = float(0)
    pValidos = float(0)
    
    total = int(input())
    brancos = int(input())
    nulos = int(input())
    validos = int(input())
    
    pBrancos = (brancos * 100) / total
    pNulos = (nulos * 100) / total
    pValidos = (validos * 100) / total
    
    print(f'BRANCOS={pBrancos:.2f} %\nNULOS={pNulos:.2f} %\nVÁLIDOS={pValidos:.2f} %')
    
    return 0
    
if __name__ == "__main__":
    main()