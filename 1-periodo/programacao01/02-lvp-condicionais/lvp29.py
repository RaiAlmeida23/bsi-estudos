"""

Tendo como dados de entrada o sexo, o peso e a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7 * h) - 58
Para mulheres: (62.1 * h) - 44.7
E que calcule seu IMC (peso dividido pelo quadrado da altura), classificando-o conforme a tabela:

IMC	Classificação
Abaixo de 17	MUITO ABAIXO DO PESO
Entre 17 e 18,49	ABAIXO DO PESO
Entre 18,50 e 24,99	PESO NORMAL
Entre 25 e 29,99	ACIMA DO PESO
Entre 30 e 34,99	OBESIDADE I
Maior que 34,99	OBESIDADE II (SEVERA)

"""

def main():
    sexo = str(0)
    peso = float(0)
    altura = float(0)
    ideal = float(0)
    imc = float(0)
    condicao = str(0)
    
    sexo = input()
    peso = float(input())
    altura = float(input())
    
    imc = peso / (altura ** 2)
    
    if(sexo.upper() == 'M'):
        ideal = (72.7 * altura) - 58
    
    else:
        ideal = (62.1 * altura) - 44.7
        
    if (imc < 17):
        condicao = "MUITO ABAIXO DO PESO"
        
    elif (imc < 19.5):
        condicao = "ABAIXO DO PESO"
        
    elif (imc < 25):
        condicao = "PESO NORMAL"
        
    elif (imc < 30):
        condicao = "ACIMA DO PESO"
        
    elif (imc < 35):
        condicao = "OBESIDADE I"
        
    else:
        condicao = "OBESIDADE II (SEVERA)"
    
    print(f'PESO IDEAL: {ideal:.2f}')
    print(f'IMC: {imc:.2f}')
    print(f'{condicao}')
    
    return 0
        
if __name__ == "__main__":
    main()