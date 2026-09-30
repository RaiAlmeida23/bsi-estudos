"""

Desenvolva um algoritmo que leia o sexo ('m' ou 'f') e a altura de 5 pessoas. Ao final, o programa deve informar:

A maior e a menor altura encontrada no grupo;
A média de altura das mulheres;
A quantidade total de homens.

"""

def main():
    sexo = str("")
    altura = float(0)
    maior = float(0)
    menor = float(0)
    somaMulheres = float(0)
    mediaMulheres = float(0)
    contMulheres = int(0)
    contHomens = int(0)

    for i in range(0, 5):
        sexo = input()
        altura = float(input())

        if(i == 0):
            maior = altura
            menor = altura

        if(altura > maior):
            maior = altura

        if(altura < menor):
            menor = altura

        if(sexo.upper() == "F"):
            somaMulheres = somaMulheres + altura
            contMulheres = contMulheres + 1

        elif(sexo.upper() == "M"):
            contHomens = contHomens + 1

    mediaMulheres = somaMulheres / contMulheres

    print(f'{maior}')
    print(f'{menor}')
    print(f'{mediaMulheres}')
    print(f'{contHomens}')

    return 0

if __name__ == "__main__":
    main()