"""

Escreva um programa que leia o peso e a altura de uma pessoa e calcule seu Índice de Massa Corporal (IMC). Fórmula do IMC: imc = peso / altura**2. Classifique o IMC conforme as regras:

"Abaixo do peso" (IMC < 18.5)
"Peso normal" (18.5 <= IMC < 24.9)
"Sobrepeso" (25 <= IMC < 29.9)
"Obesidade" (IMC >= 30)

"""

def main():
    peso = int(0)
    altura = float(0.0)
    imc = float(0.0)
    
    peso = int(input())
    altura = float(input())
    
    imc = peso / altura**2
    
    if(imc < 18.5):
        print(f'Abaixo do peso')
        
    elif(imc >= 18.5 and imc <= 24.9):
        print(f'Peso normal')
        
    elif(imc >= 25 and imc <= 29.9):
        print(f'Sobrepeso')
    
    elif(imc >= 30):
        print(f'Obesidade')
    
    return 0
    
if __name__ == "__main__":
    main()