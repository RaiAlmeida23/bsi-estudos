"""

Desenvolva um algoritmo que percorra os números de 0 até 10 utilizando o comando for. 
Para cada número, utilize o operador de resto (%) para verificar se ele é par e, em caso positivo, escreva-o na tela.

"""

def main():
    
    for i in range(0, 11):
        if(i % 2 == 0):
            print(f'{i}')
    
    return 0
    
if __name__ == "__main__":
    main()