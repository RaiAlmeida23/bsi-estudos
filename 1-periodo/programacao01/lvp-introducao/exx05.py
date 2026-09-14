# Desenvolva um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias. 
# O programa deve calcular o total de dias que essa pessoa já viveu e exibir esse valor acumulado. 
# Para este cálculo, considere obrigatoriamente que um ano possui 365 dias e um mês possui 30 dias.

def main():
    anos = int(0)
    meses = int(0)
    dias = int(0)
    idade = int(0)
    
    anos = int(input())
    meses = int(input())
    dias = int(input())
    
    idade = (anos * 365) + (meses * 30) + dias
    
    print(f'{idade}')
    
    return 0
    
if __name__ == "__main__":
    main()