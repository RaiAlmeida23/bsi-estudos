"""

Escreva um programa que leia a temperatura em graus Celsius e classifique como:

“Muito frio” (abaixo de 0)
“Frio” (0 a 10)
“Agradável” (11 a 25)
“Quente” (26 a 35)
“Muito quente” (acima de 35)

"""

def main():
    tem = int(0)
    
    tem = int(input())
    
    if(tem < 0):
        print(f'Muito frio')
        
    elif(tem >= 0 and tem <= 10):
        print(f'Frio')
        
    elif(tem >= 11 and tem <= 25):
        print(f'Agradável')
        
    elif(tem >= 26 and tem <= 35):
        print(f'Quente')
        
    elif(tem > 34):
        print(f'Muito quente')
    
    return 0
    
if __name__ == "__main__":
    main()