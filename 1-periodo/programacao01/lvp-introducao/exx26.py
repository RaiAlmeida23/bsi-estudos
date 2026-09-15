"""

Desenvolva um algoritmo que leia dois números inteiros e os armazene, respectivamente, em uma variável denominada a e 
em outra denominada b. O programa deve processar a troca real e física dos valores contidos na memória dessas variáveis, 
fazendo com que o conteúdo original de b passe para a e o conteúdo original de a passe para b.

"""

def main():
    a = int(0)
    b = int(0)
    aux = int(0)
    
    a = int(input())
    b = int(input())
    
    aux = a
    a = b
    b = aux
    
    print(f'{a} e {b}')
    
    return 0
    
if __name__ == "__main__":
    main()