"""

Faça um programa que receba três números inteiros representando o dia, o mês e o ano, e retorne uma data completa formatada no padrão DD/MM/AAAA.
Consulte como preencher valores com zeros à esquerda no material da disciplina: Guia de Programação: Entrada e Saída de Dados em Python.
Formatação da Saída: A mensagem deve ser exibida exatamente no padrão A data informada é DD/MM/AAAA., garantindo que dias e meses menores que 10 
contenham o zero à esquerda e que a frase termine com ponto final.

"""

def main():
    dia = int(0)
    mes = int(0)
    ano = int(0)
    
    dia = int(input())
    mes = int(input())
    ano = int(input())
    
    print(f'A data informada é {dia:02d}/{mes:02d}/{ano}')
    
    return 0
    
if __name__ == "__main__":
    main()