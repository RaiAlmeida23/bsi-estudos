"""

Faça um programa que receba um valor monetário em reais (R$) e calcule a sua conversão para dólares americanos (U$), utilizando uma taxa cambial fixada em 4.50.
dolares = reais / 4.50
Formatação da Saída: O resultado convertido deve ser precedido pelo símbolo U$ e formatado com exatamente duas casas decimais.

"""

def main():
    reais = float(0.0)
    dolar = float(0.0)
    
    reais = float(input())
    
    dolar = reais / 4.50
    
    print(f'U$ {dolar:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()