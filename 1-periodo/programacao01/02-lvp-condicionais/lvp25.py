"""

Faça um programa, em Python 3.x, que leia um valor inteiro entre 1000 (MIL) e 9999 (NOVE MIL NOVECENTOS E NOVENTA E NOVE) (inclusive os dois valores) e, 
utilizando apenas recursos matemáticos (DIV: // e MOD: %) que já aprendemos em sala de aula, inverta esse número, entregando um valor inteiro como resposta 
(NÃO É PERMITIDO UTILIZAR QUALQUER RECURSO DE STRING OU MÉTODO/FUNÇÃO NÃO APRENDIDOS E USADOS NA DISCIPLINA). Ao final, o programa deverá verificar se o 
valor digitado é uma CAPICUA, imprimindo a informação conforme os casos de teste.

CAPICUA: sequência de algarismos que permanece a mesma se lida na ordem direta ou inversa (p.ex., 13231).

"""

def main():
    num = int(0)
    uni = int(0)
    dez = int(0)
    cen = int(0)
    mil = int(0)
    invertido = int(0)
    
    num = int(input())
    
    uni = num % 10
    dez = (num // 10) % 10
    cen = (num // 100) % 10
    mil = (num // 1000) % 10
    invertido = (uni * 1000) + (dez * 100) + (cen * 10) + mil
    
    if(num == invertido):
        print(f'{num} É UMA CAPICUA')
        
    else:
        print(f'{num} NÃO É UMA CAPICUA')

    return 0

if __name__ == "__main__":
    main()