"""

Adiciona-se um dia extra ao calendário para compensar a diferença entre o ano convencional e o ano trópico, que é baseado no tempo que 
a Terra leva para completar uma órbita ao redor do Sol, utilizando o equinócio vernal como referência. Enquanto o ano trópico tem 
aproximadamente 365,2422 dias solares, o ano convencional tem apenas 365 dias solares. Isso resulta em um excedente de aproximadamente 
5 horas, 48 minutos e 46 segundos (0,2422 dia) a cada ano trópico. As horas extras são acumuladas e adicionadas ao calendário como um dia 
completo (4 vezes 6 horas equivalem a 1 dia).

No calendário Gregoriano, esse dia extra é inserido no final do mês de fevereiro, que passa a ter 29 dias (ano com 366 dias) em vez dos 
28 dias dos anos normais (ano com 365 dias).

Regras para o ano BISSEXTO:

1) Deve ser divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero, porém não pode ser divisível por 100. 
Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
2) Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
Com base nessas informações faça um programa que leia um ano e informe se ele é bissexto ou não.

"""

def main():
    ano = int(0)
    
    ano = int(input())
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'{ano} É BISSEXTO') 
        
    else:
        print(f'{ano} NÃO É BISSEXTO') 
    
    return 0

if __name__ == "__main__":
    main()