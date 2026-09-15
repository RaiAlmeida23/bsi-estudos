"""

Faça um programa que receba dois números e mostre a soma dos cubos desses números dividida pela soma desses dois números. 

"""

def main():
    n1 = int(0)
    n2 = int(0)
    soma = float(0.0)
    
    n1 = int(input())
    n2 = int(input())
    
    soma = ((n1 ** 3) + (n2 ** 3)) / (n1 + n2)
    
    print(f'{soma:.2f}')
    
    return 0
    
if __name__ == "__main__":
    main()