"""

Escreva um programa que leia a pressão arterial sistólica de uma pessoa e classifique o risco de hipertensão, conforme as regras:

Menor que 120: Pressão normal
De 120 a 129: Elevada
De 130 a 139: Hipertensão estágio 1
140 ou mais: Hipertensão estágio 2

"""

def main():
    pressao = int(0)
    
    pressao = int(input())
    
    if(pressao < 120):
        print(f'Pressão normal')
        
    elif(pressao >= 120 and pressao <= 129):
        print(f'Elevada')
        
    elif(pressao >= 130 and pressao <= 139):
        print(f'Hipertensão estágio 1')
        
    elif(pressao >= 140):
        print(f'Hipertensão estágio 2')
    
    return 0
    
if __name__ == "__main__":
    main()