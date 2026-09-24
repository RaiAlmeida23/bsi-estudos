"""

Desenvolva um algoritmo que solicite números inteiros ao usuário até que o valor 0 (zero) seja digitado. 
Ao final, o programa deve calcular e exibir a média aritmética de todos os números fornecidos (excluindo o zero da contagem).

"""

def main():
    num = int(0)
    soma = int(0)
    cont = int(0)
    media = float(0)

    num = int(input())

    while(num != 0):
        soma = soma + num
        cont = cont + 1

        num = int(input())

    if(cont > 0):
        media = soma / cont
    else:
        media = 0.0

    print(f'{media}')

    return 0

if __name__ == "__main__":
    main()
