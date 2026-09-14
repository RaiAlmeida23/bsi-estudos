"""

Desenvolva um algoritmo que leia um valor de temperatura em graus Fahrenheit, realize a conversão para graus Celsius 
utilizando a fórmula padrão e exiba o resultado arredondado com exatamente duas casas decimais.

"""

def main():
    tempF = float(0.0)
    tempC = float(0.0)
    
    tempF = float(input())
    
    tempC = (tempF - 32) * (5/9)
    
    print(f'{tempC:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()