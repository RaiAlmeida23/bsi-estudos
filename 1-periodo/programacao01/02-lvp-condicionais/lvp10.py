"""

Leia o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu). 
Considere o ano atual como 2024 e a idade mínima, para votar, 16 anos.

"""

def main():
    ano = int(0)
    idade = int(0)
    
    ano = int(input())
    
    idade = 2024 - ano
    
    if (idade >= 16):
        print(f'{idade} anos: PODE VOTAR') 
        
    else:
        print(f'{idade} anos: NÃO PODE VOTAR') 
    
    return 0

if __name__ == "__main__":
    main()