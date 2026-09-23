"""

Desenvolva um programa que percorra todos os números inteiros no intervalo de 0 a 10 (inclusive). 
Para cada número encontrado, o algoritmo deve verificar, utilizando operadores matemáticos, se ele é par. 
Caso seja, o número deve ser impresso na tela.

"""

def main():
    i = int(0)
    
    while(i <= 10):
        if (i % 2 == 0):
            print(f'{i}')
        
        i = i + 1
    
    return 0
    
if __name__ == "__main__":
    main()