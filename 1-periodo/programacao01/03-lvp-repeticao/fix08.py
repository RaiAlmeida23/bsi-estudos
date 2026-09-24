"""

Desenvolva um algoritmo que solicite ao usuário uma sequência de números inteiros. 
O programa deve contar quantos números positivos e quantos números negativos foram inseridos. 
A entrada encerra-se quando o valor 0 (zero) for digitado.

"""

def main():
    num = int(0)
    contN = int(0)
    contP = int(0)
    
    num = int(input())
    while(num != 0):
        if(num > 0):
            contP = contP + 1
        elif(num < 0):
            contN = contN + 1
            
        num = int(input())
    
    print(f'{contP} {contN}')
    
    return 0
    
if __name__ == "__main__":
    main()