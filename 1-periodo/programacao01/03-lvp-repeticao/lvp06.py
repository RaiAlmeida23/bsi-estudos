"""

Desenvolva um algoritmo que realize a leitura de uma série de números inteiros. 
O processo de leitura deve ser repetido enquanto o usuário desejar (utilizando 's' para continuar e 'n' para encerrar). 
Ao finalizar a entrada de dados, o programa deve calcular e exibir a média aritmética de todos os valores informados.

"""

def main():
    flag = ''
    n = int(0)
    soma = int(0)
    cont = int(0)
    media = float(0.0)
    
    flag = input()
    
    while(flag.upper() == "S"):
        n = int(input())
        soma = soma + n
        cont = cont + 1
        flag = input()
        
    media = soma / cont
    print(f'{media:.1f}')
    
    return 0
    
if __name__ == "__main__":
    main()