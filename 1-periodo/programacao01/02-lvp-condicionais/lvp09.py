"""

Ler um valor inteiro e escrever se é positivo ou negativo (só para efeitos desse programa, considere o valor zero como positivo).

"""

def main():
    num = int(0)
    
    num = int(input())
    
    if (num >= 0):
        print(f'POSITIVO') 
        
    else:
        print(f'NEGATIVO') 
    
    return 0

if __name__ == "__main__":
    main()