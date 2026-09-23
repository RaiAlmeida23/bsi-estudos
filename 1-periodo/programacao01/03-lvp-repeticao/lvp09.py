"""

Escreva um algoritmo que realize a leitura de 5 valores inteiros fornecidos pelo usuário. 
Ao final da leitura, o programa deve calcular e exibir a média aritmética desses valores.

"""

def main():
    valor = int(0)
    soma = int(0)
    media = int(0)
    i = int(0)
    
    i = 1
    while(i <= 5):
        valor = int(input())
        soma = soma + valor
        i = i + 1
    
    media = soma / 5
    print(f'{media:.0f}')
    
    return 0
    
if __name__ == "__main__":
    main()