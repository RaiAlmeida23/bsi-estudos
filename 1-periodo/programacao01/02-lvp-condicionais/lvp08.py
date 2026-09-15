"""

Elaborar um programa que efetue a leitura de um número inteiro e efetue a sua apresentação, caso o valor não seja divisível por três.

"""

def main():
    num = int(0)
    
    num = int(input())
    
    if (num % 3 != 0):
        print(f'{num}') 
    
    return 0

if __name__ == "__main__":
    main()