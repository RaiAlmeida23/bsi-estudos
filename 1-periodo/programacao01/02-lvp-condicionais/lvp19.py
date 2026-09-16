"""

A jornada de trabalho semanal de um funcionário é de 40 horas. 
O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. 
Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, 
que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas, totalizando o 
esperado de 160h/mês).

Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    hTrab = int(0)
    salario = float(0)
    extras = int(0)
    total = float(0)
    
    hTrab = int(input())
    salario = float(input())
    
    if (hTrab > 160):
        extras = hTrab - 160
        total = (160 * salario) + extras * (salario + (salario/2))
    
    else:
        total = hTrab * salario

    print(f'{total:.1f}')
    
    return 0

if __name__ == "__main__":
    main()