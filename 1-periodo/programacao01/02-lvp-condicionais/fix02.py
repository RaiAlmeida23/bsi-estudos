"""

Escreva um programa que leia a nota de um trabalho e o número de dias de atraso na entrega. 
Para cada dia de atraso, deve ser descontado 10% da nota. A nota final não pode ser inferior a zero.

"""

def main():
    trabalho = int(0)
    dias = int(0)
    desconto = float(0)
    nota = float(0)
    
    trabalho = int(input())
    dias = int(input())
    
    desconto = (trabalho * (10 * dias)) / 100
    nota = trabalho - desconto
    
    if(nota < 0):
        nota = 0
        
    if(dias == 0):
        nota = trabalho
        
    print(f'Nota final: {nota:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()