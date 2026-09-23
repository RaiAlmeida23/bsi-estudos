"""

Desenvolva um algoritmo que seja capaz de imprimir na tela uma sequência numérica progressiva, iniciando no valor 0 e finalizando no valor 9. 
Cada número deve ser apresentado em uma nova linha.

"""

def main():
    i = int(0)
    
    while(i < 10):
        print(f'{i}')
        i = i + 1
    
    return 0
    
if __name__ == "__main__":
    main()