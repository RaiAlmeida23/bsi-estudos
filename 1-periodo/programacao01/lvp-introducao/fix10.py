"""

Faça um programa que receba uma distância em quilômetros (km) e converta esse valor para milhas, sabendo que 1 km = 0.621371 milhas. A relação matemática a ser aplicada é:
milhas = km * 0.621371
Formatação da Saída: O resultado final deve ser exibido no formato {km}Km = {milhas} milhas, com a distância em milhas formatada obrigatoriamente com quatro casas decimais.

"""

def main():
    km = int(0)
    milhas = float(0.0)
    
    km = int(input())
    
    milhas = km * 0.621371
    
    print(f'{km}Km = {milhas:.4f} milhas')
    
    return 0
    
if __name__ == "__main__":
    main()