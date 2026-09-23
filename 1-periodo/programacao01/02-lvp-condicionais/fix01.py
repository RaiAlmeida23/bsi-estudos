"""

Escreva um programa que leia a hora do dia (em formato 24 horas) e informe se está dentro do horário comercial (das 9h às 18h) ou fora do horário comercial.

"""

def main():
    hora = int(0)
    
    hora = int(input())
    
    if(hora >= 9 and hora <= 18):
        print(f'Dentro do horário comercial')
        
    else:
        print(f'Fora do horário comercial')
    return 0

if __name__ == "__main__":
    main()