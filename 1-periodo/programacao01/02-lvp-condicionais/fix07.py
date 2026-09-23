"""

Escreva um programa que leia o salário de uma pessoa e calcule o valor do imposto de renda com base nas seguintes faixas:

Até R$ 1903,98: Isento
De R$ 1903,99 a R$ 2826,65: 7.5%
De R$ 2826,66 a R$ 3751,05: 15%
De R$ 3751,06 a R$ 4664,68: 22.5%
Acima de R$ 4664,68: 27.5%

"""

def main():
    salario = int(0)
    imposto = int(0)
    
    salario = int(input())
    
    if(salario <= 1903.98):
        print(f'Isento')
    
    else:    
        if(salario >= 1903.99 and salario <= 2826.65):
            imposto = salario * 0.075
            
        elif(salario >= 2826.66 and salario <= 3751.05):
            imposto = salario * 0.15
        
        elif(salario >= 3751.06 and salario <= 4664.68):
            imposto = salario * 0.225
            
        elif(salario >= 4664.68):
            imposto = salario * 0.275
            
        print(f'Imposto: R$ {imposto:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()