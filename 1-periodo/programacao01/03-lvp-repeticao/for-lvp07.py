"""

Desenvolva um algoritmo que leia um valor inteiro e escreva a sua tabuada de multiplicação de 1 a 10. 
Utilize obrigatoriamente o comando for iniciando o range em 0.

"""

def main():
    num = int(0)
    i = int(0)
    
    num = int(input())
    
    for i in range(1, 11, 1):
        print(f'{i} x {num} = {i * num}')
        
    return 0
    
if __name__ == "__main__":
    main()