"""

Faça um programa, em Python 3.x, que solicite a idade e o peso ao usuário, então, calcule e informe a quantidade de água (em litros, 
com uma casa decimal) que essa pessoa deve consumir ao longo do dia, de acordo com a tabela de referência:

Faixa Etária	Quantidade de Água por kg
Jovens até os 17 anos	40 ml por cada kg
18 a 55 anos	35 ml por cada kg
56 a 65 anos	30 ml por cada kg
66 anos em diante	25 ml por cada kg

"""

def main():
    idade = int(0)
    peso = int(0)
    
    listros = float(0)
    
    idade = int(input())
    peso = int(input())
    
    if(idade <= 17):
        litros = (peso * 40) / 1000
    
    elif(idade >= 18 and idade <= 55):
        litros = (peso * 35) / 1000
    
    elif(idade >= 56 and idade <= 65):
        litros = (peso * 30) / 1000
        
    elif(idade >= 66 ):
        litros = (peso * 25) / 1000
        
    print(f'{litros:.1f} LITROS')
    
    return 0

if __name__ == "__main__":
    main()