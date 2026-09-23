"""

Desenvolva um programa que realize a leitura de diversos números de forma indeterminada. 
Para cada número inserido, o sistema deve perguntar ao usuário se ele deseja continuar informando dados. 
O usuário utilizará a letra 's' para continuar e 'n' para encerrar. 
Ao final, o algoritmo deve exibir o valor total da soma de todos os números lidos.

"""

def main():
    n = int(0)
    soma = int(0)
    flag = ''
    
    flag = input()
    
    while(flag.upper() == "S"):
        n = int(input())
        soma = soma + n
        flag = input()
        
    print(f'{soma}')
    
    return 0
    
if __name__ == "__main__":
    main()