"""

Um número de Armstrong é um número de N dígitos onde a soma de cada dígito, elevado a N, é igual ao próprio número. 
Escreva um programa que leia números inteiros de 100 a 9999 e verifique se é um número de Armstrong, utilizando apenas DIV (//) e MOD (%) e operadores matemáticos.

"""

def main():
    uni = int(0)
    dez = int(0)
    cen = int(0)
    mil = int(0)
    num = int(0)
    som = int(0)
    
    num = int(input())
    
    uni = num % 10
    dez = (num // 10) % 10
    cen = (num // 100) % 10
    mil = (num // 1000) % 10
    
    if(num < 1000):
        som = (uni**3) + (dez**3) + (cen**3)
            
    else:
        som = (uni**4) + (dez**4) + (cen**4) + (mil**4)
    
    if (num == som):
         print(f"{num} É UM NÚMERO DE ARMSTRONG")
            
    else:
        print(f"{num} NÃO É UM NÚMERO DE ARMSTRONG")
    
    return 0
    
if __name__ == "__main__":
    main()