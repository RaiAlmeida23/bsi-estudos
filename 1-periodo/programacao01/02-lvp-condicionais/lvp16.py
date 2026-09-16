"""

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
Até 20 litros, desconto de 3%
Acima 20 litros, desconto de 5%

Gasolina:
Até 20 litros, desconto de 4%
Acima 20 litros, desconto de 6%

Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool ou G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    litros = int(0)
    tipo = ''
    
    desconto = float(0.0)
    valor = float(0.0)
    
    litros = int(input())
    tipo = input().upper()
    
    if(tipo == 'A'):
        if(litros <= 20):
            desconto = ((litros * 2.90) * 3) / 100
            
        elif(litros > 20):
            desconto = ((litros * 2.90) * 5) / 100
        
        valor = (litros * 2.90) - desconto
        
    elif(tipo == 'G'):
        if(litros <= 20):
            desconto = ((litros * 3.30) * 4) / 100
            
        elif(litros > 20):
            desconto = ((litros * 3.30) * 6) / 100
            
        valor = (litros * 3.30) - desconto
        
    
    print(f'{valor:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()