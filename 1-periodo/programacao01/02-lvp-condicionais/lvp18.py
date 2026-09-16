"""

Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos), em formato 24h. 
Calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
Nota: A saída deve ser idêntica ao exemplo do output, cuidado com as formatações.

"""

def main():
    inicio = int(0)
    termino = int(0)
    duracao = int(0)
    aux = int(0)
    
    inicio = int(input())
    termino = int(input())
    
    if (inicio < termino):
        duracao = termino - inicio
        
    else:
        duracao = (24 - inicio) + termino
        
    print(f'{duracao}')
    
    return 0

if __name__ == "__main__":
    main()