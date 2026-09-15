"""

Desenvolva um algoritmo que leia dois números inteiros. 
O programa deve elevar cada um deles ao quadrado, somar os resultados e, por fim, calcular a raiz quadrada dessa soma. 
O resultado final deve ser exibido com duas casas decimais.

"""

def main():
    num1 = int(0)
    num2 = int(0)
    
    quad1 = int(0)
    quad2 = int(0)
    raiz = float(0)
    
    num1 = int(input())
    num2 = int(input())
    
    quad1 = num1 ** 2
    quad2 = num2 ** 2
    
    raiz = (quad1 + quad2) ** (0.5)
    
    print(f'{raiz:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()