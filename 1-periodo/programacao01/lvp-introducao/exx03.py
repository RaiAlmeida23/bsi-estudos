# Desenvolva um algoritmo que realize a leitura de um valor inteiro fornecido via teclado. 
# O programa deve calcular o seu antecessor (o número que vem imediatamente antes dele na sequência numérica) e exibir esse resultado na tela.

def main():
    num = int(0)
    ant = int(0)
    
    num = int(input())
    
    ant = num - 1
    
    print(f'{ant}')
    
    return 0
    
if __name__ == "__main__":
    main()
