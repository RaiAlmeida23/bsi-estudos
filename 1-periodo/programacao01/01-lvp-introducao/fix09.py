"""

Faça um programa que receba o raio e a altura de um cilindro e calcule o seu volume através da fórmula:
volume = 3.14159 * (raio ** 2) * altura
Considere a constante pi = 3.14159
Formatação da Saída: O resultado final deve ser precedido pelo rótulo Volume= e formatado com exatamente 3 casas decimais.

"""

def main():
    raio = float(0.0)
    altura = float(0.0)
    volume = float(0.0)
    
    raio = float(input())
    altura = float(input())
    
    volume = 3.14159 * (raio ** 2) * altura
    
    print(f'Volume={volume:.3f}')
    
    return 0
    
if __name__ == "__main__":
    main()