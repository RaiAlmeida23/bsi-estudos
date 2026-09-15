"""

Ler quatro valores referentes a quatro notas escolares (0 a 100) de um aluno e escrever uma mensagem dizendo que o aluno foi APROVADO 
se o valor da média escolar for maior ou igual a 60. Se o aluno teve média inferior a 60 e maior ou igual a 20, informar que ele está 
de PROVA FINAL; se o aluno teve média inferior a 20, informar que ele está REPROVADO.

Formatação da Saída: O resultado deve exibir a situação do aluno (APROVADO, PROVA FINAL ou REPROVADO) acompanhada da média calculada 
com exatidão de duas casas decimais (ex: PROVA FINAL com média 46.00).

"""

def main():
    n1 = float(0)
    n2 = float(0)
    n3 = float(0)
    n4 = float(0)
    media = float(0)
    
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    
    media = (n1 + n2 + n3 + n4)/4
    
    if(media >= 60):
        print(f'APROVADO com média {media:.2f}')
    
    elif(media <= 60 and media >= 20):
        print(f'PROVA FINAL com média {media:.2f}')
        
    else:
        print(f'REPROVADO com média {media:.2f}')
        
    return 0

if __name__ == "__main__":
    main()