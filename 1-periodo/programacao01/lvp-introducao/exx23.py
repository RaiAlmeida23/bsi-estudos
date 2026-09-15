"""

Desenvolva um algoritmo que receba quatro notas de um aluno (valores de 0 a 100), inseridas uma por linha. 
O programa deve realizar o somatório dessas notas, calcular a sua média aritmética simples e exibir a mensagem 
padrão correspondente com o resultado formatado em duas casas decimais.

"""

def main():
    n1 = float(0.0)
    n2 = float(0.0)
    n3 = float(0.0)
    n4 = float(0.0)
    media = float(0.0)
    
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    
    media = (n1+n2+n3+n4) / 4
    
    print(f'A média aritmética, dos valores fornecidos, é {media:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()