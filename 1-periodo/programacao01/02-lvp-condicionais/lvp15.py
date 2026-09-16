"""

Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo e qual tipo de triângulo é. 
Orientação importante: primeiro teste se os valores formam um triângulo. 
Para formar um triângulo, o valor de cada lado deve ser menor que a soma dos outros 2 lados.
Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    a = int(0)
    b = int(0)
    c = int(0)
    
    a = int(input())
    b = int(input())
    c = int(input())
    
    if (a < (b + c) and b < (a + c) and c < (a + b)):
        if(a == b and a == c and b == c):
            print(f'EQUILÁTERO')
        
        elif((a == b and a != c) or (b == c and b != a) or (c == a and c != b)):
            print(f'ISÓSCELES')
            
        elif(a != b and a != c and b != c):
            print(f'ESCALENO')
        
    else:
        print(f'NÃO É TRIÂNGULO')
    
    return 0
    
if __name__ == "__main__":
    main()