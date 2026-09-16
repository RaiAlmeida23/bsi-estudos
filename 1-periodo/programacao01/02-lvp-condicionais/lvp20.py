"""

Tendo como dados de entrada a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas:

Para sexo masculino: peso ideal = (72.7 * altura) - 58
Para sexo feminino: peso ideal = (62.1 * altura) - 44.7
Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    sexo = ''
    altura = float(0)
    peso = float(0)
    
    tipo = input().upper()
    altura = float(input())
    
    if (tipo == 'M'):
        peso = (72.7 * altura) - 58
            
    elif (tipo == 'F'):
        peso = (62.1 * altura) - 44.7
        
    print(f'{peso:.3f}')
    
    return 0

if __name__ == "__main__":
    main()