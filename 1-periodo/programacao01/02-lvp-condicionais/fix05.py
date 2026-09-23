"""

Escreva um programa que leia a idade de um atleta e determine a sua categoria na natação, conforme as regras:

Até 10 anos: Infantil.
De 11 a 15 anos: Juvenil.
De 16 a 20 anos: Júnior.
De 21 a 30 anos: Profissional.
Acima de 30 anos: Sênior.

"""

def main():
    idade = int(0)
    
    idade = int(input())
    
    if(idade <= 10):
        print(f'Categoria: Infantil')
        
    elif(idade >= 11 and idade <= 15):
        print(f'Categoria: Juvenil')
        
    elif(idade >= 16 and idade <= 20):
        print(f'Categoria: Júnior')
        
    elif(idade >= 21 and idade <= 30):
        print(f'Categoria: Profissional')
        
    elif(idade > 30):
        print(f'Categoria: Sênior')
    
    return 0
    
if __name__ == "__main__":
    main()