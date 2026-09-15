"""

Desenvolva um algoritmo que leia a idade de uma pessoa expressa em um valor inteiro total de dias. 
O programa deve fracionar e exibir essa idade convertida em anos, meses e dias. 
Para os cálculos lógicos deste problema, adote estritamente as convenções de que 1 ano possui sempre 365 dias e 1 mês possui sempre 30 dias.

"""

def main():
    idade = int(0)
    anos = int(0)
    meses = int(0)
    dias = int(0)
    
    idade = int(input())
    
    anos = idade // 365
    meses = (idade % 365) // 30
    dias = (idade % 365) % 30
    
    print(f'{anos} anos, {meses} meses e {dias} dias')
    
    return 0
    
if __name__ == "__main__":
    main()