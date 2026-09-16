"""

Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de segundo grau, apresentando as duas raízes, 
se para os valores informados for possível efetuar o referido cálculo. Lembre-se de que a variável A deve ser diferente de zero.
Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    a = float(0)
    b = float(0)
    c = float(0)
    delta = float(0)
    x1 = float(0)
    x2 = float(0)
    
    a = int(input())
    b = int(input())
    c = int(input())
    
    if (a != 0):
        delta = (b ** 2) - (4 * a * c)
        
        if (delta < 0):
            print('Não há raízes reais')
            
        elif (delta == 0):
            x1 = -b / (2 * a)
            print(f'{x1:.1f}')
            
        else:
            x1 = (-b + (delta ** 0.5)) / (2 * a)
            x2 = (-b - (delta ** 0.5)) / (2 * a)
            print(f'{x1:.1f} {x2:.1f}')
       
    
    return 0

if __name__ == "__main__":
    main()