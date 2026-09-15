"""

Desenvolva um algoritmo que receba o valor ganho por hora e a quantidade de horas trabalhadas no mês (um valor por linha). 
O programa deve calcular o Salário Bruto e, com base nele, aplicar os seguintes percentuais fixos de desconto:

Imposto de Renda (IR): 11% sobre o bruto
INSS: 8% sobre o bruto
Sindicato: 5% sobre o bruto
Ao final, subtraia a soma de todos os descontos do Salário Bruto para computar o Salário Líquido.

"""

def main():
    pHora = float(0.0)
    qtdHora = int(0)
    
    bruto = float(0.0)
    ir = float(0.0)
    inss = float(0.0)
    sindicato = float(0.0)
    liquido = float(0.0)
    
    pHora = float(input())
    qtdHora = int(input())
    
    bruto = pHora * qtdHora
    ir = (bruto * 11) / 100
    inss = (bruto * 8) / 100
    sindicato = (bruto * 5) / 100
    liquido = bruto - ir - inss - sindicato
    
    print(f'+ Salário Bruto : R$ {bruto:.2f}\n- IR (11%) : R$ {ir:.2f}\n- INSS (8%) : R$ {inss:.2f}\n- Sindicato (5%) : R$ {sindicato:.2f}\n= Salário Líquido : R$ {liquido:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()