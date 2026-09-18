"""

Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    fixo = float(0.0)
    vendas = float(0.0)
    
    comissao = float(0.0)
    salario = float(0.0)
    
    fixo = float(input())
    vendas = float(input())
    
    if(vendas <= 1500):
        comissao = (vendas * 3) / 100

    elif(vendas > 1500):
        comissao = ((1500 * 3) / 100) + (((vendas-1500) * 5) / 100)

    salario = fixo + comissao 
    print(f'{salario:.1f}')
    
    return 0
    
if __name__ == "__main__":
    main()