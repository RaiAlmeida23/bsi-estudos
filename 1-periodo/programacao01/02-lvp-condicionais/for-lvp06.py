"""

Desenvolva um algoritmo que leia 5 valores inteiros. Ao final, o programa deve calcular e apresentar a média aritmética. 
A repetição deve iniciar o índice em 0 e a função principal deve retornar um status de finalização.

"""

def main():
    num = int(0)
    soma = int(0)
    i = int(0)
    
    for i in range(0, 5, 1):
        num = int(input())
        soma = soma + num
    
    print(f'{soma/(i+1):.0f}')
    
    return 0
    
if __name__ == "__main__":
    main()