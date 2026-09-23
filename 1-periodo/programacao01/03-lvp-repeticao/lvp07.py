"""

Desenvolva um programa que realize a leitura de um valor inteiro. 
O algoritmo deve calcular e exibir na tela a tabuada de multiplicação desse valor, abrangendo o intervalo de 1 até 10.

"""

def main():
    valor = int(0)
    i = int(0)
    
    valor = int(input())
    
    i = 1
    while(i <= 10):
        print(f'{i} X {valor} = {i * valor}')
        i = i + 1
    
    return 0
    
if __name__ == "__main__":
    main()