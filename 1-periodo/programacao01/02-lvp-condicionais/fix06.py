"""

Escreva um programa que leia a velocidade de um veículo e classifique-o em uma das seguintes categorias:

Abaixo de 40 km/h: "Muito Lento"
Entre 40 km/h e 60 km/h: "Lento"
Entre 61 km/h e 80 km/h: "Velocidade Permitida"
Entre 81 km/h e 100 km/h: "Acima do Limite"
Acima de 100 km/h: "Multa Grave"

"""

def main():
    velocidade = int(0)
    
    velocidade = int(input())
    
    if(velocidade < 40):
        print(f'Muito Lento')
        
    elif(velocidade >= 40 and velocidade <= 60):
        print(f'Lento')
        
    elif(velocidade >= 61 and velocidade <= 80):
        print(f'Velocidade Permitida')
    
    elif(velocidade >= 81 and velocidade <= 100):
        print(f'Acima do Limite')
    
    elif(velocidade > 100):
        print(f'Multa Grave')
    
    return 0
    
if __name__ == "__main__":
    main()