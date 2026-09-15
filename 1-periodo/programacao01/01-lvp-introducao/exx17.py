"""

Desenvolva um algoritmo que leia o salário mensal atual de um funcionário e o percentual de reajuste. 
O programa deve calcular o valor do aumento e exibir o valor do novo salário.

"""

def main():
    salario = float(0.0)
    reajuste = float(0.0)
    
    aumento = float(0.0)
    novo_salario = float(0.0)
    
    salario = float(input())
    reajuste = float(input())
    
    aumento = (salario * reajuste) // 100
    novo_salario = round((salario + aumento), 2)
    
    print(f'{novo_salario}')
    
    return 0
    
if __name__ == "__main__":
    main()