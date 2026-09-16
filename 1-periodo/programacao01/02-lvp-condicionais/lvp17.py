"""

Ler 3 valores inteiros: a, b e c (considere que não serão informados valores iguais).
Utilizando o algoritmo de troca de valores entre variáveis, vistos na LVP INTRODUÇÃO 26: TROCAR VALORES, realocar os valores das variáveis, fazendo com que o menor valor esteja na variável a, o segundo menor valor na variável b e o maior valor na variável c.
A saída do programa deve ser, obrigatoriamente, com a linha abaixo:
print(f'{a} {b} {c}')

"""

def main():
    a = int(0)
    b = int(0)
    c = int(0)
    aux = int(0)
    aux1 = int(0)
    
    a = int(input())
    b = int(input())
    c = int(input())
    
    if (a < b and a < c):
        if(b < c):
           a = a
           b = b
           c = c
           
        else:
            aux = b
            b = c
            c = aux
            
    elif (b < c and b < a):
        if(c < a):
            aux = a
            a = b
            b = c
            c = aux
            
        else:
            aux = a
            a = b
            b = aux
    
    elif (c < a and c < b):
        if(a < b):
            aux = a 
            a = c  
            aux1 = b
            b = aux       
            c = aux1       
            
        else:
            aux = a 
            a = c  
            c = aux
            
    print(f'{a} {b} {c}')
    
    return 0

if __name__ == "__main__":
    main()