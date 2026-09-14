"""

Desenvolva um algoritmo que leia a quantidade de carros vendidos, o valor total de vendas, o salário fixo mensal e a comissão por carro, de um vendedor. 
O programa deve calcular e exibir o salário final obtido com precisão de duas casas decimais, sabendo que o vendedor recebe, também, 5% do valor total de vendas.

"""

def main():
    qtd_carros = int(0)
    vendas = float(0.0)
    salario_fixo = float(0.0)
    comissao = float(0.0)
    
    salario = float(0.0)
    
    qtd_carros = int(input())
    vendas = float(input())
    salario_fixo = float(input())
    comissao = float(input())
    
    salario = salario_fixo + (comissao * qtd_carros) + ((vendas * 5) // 100) 
    
    print(f'{salario:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()