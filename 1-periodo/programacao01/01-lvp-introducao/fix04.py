"""

Faça um programa que receba o peso (em kg) e a altura (em metros) de uma pessoa e calcule o seu Índice de Massa Corporal (IMC), aplicando a seguinte fórmula:
imc = peso / (altura ** 2)

"""

def main():
    peso = float(0.0)
    altura = float(0.0)
    imc = float(0.0)
    
    peso = float(input())
    altura = float(input())
    
    imc = peso / (altura ** 2)
    
    print(f'imc={imc:.3f}')
    
    return 0

if __name__ == "__main__":
    main()