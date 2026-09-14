# Desenvolva um programa que solicite ao usuário as dimensões de um retângulo: a base e a altura. 
# O algoritmo deve calcular a área total da figura (base multiplicada pela altura) e exibir o resultado final formatado.

def main():
    base = float(0.0)
    altura = float(0.0)
    area = float(0.0)
    
    base = float(input())
    altura = float(input())
    
    area = base * altura
    
    print(f'{area:.1f}')
    
    return 0
    
if __name__ == "__main__":
    main()
