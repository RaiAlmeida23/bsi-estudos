"""

Desenvolva um algoritmo que leia a aceleração escalar constante (a) e o tempo decorrido (t) 
de um veículo em movimento retilíneo, inseridos um por linha. Sabendo que o veículo parte do repouso 
(o que determina que a velocidade inicial v0=0 e a posição inicial s0=0), o programa deve calcular:

A velocidade escalar final (v) utilizando a fórmula: v=v0+a⋅t
A distância percorrida (s) utilizando a fórmula: s=s0+v0⋅t+12⋅a⋅t2

"""

def main():
    aceleracao = float(0.0)
    tempo = float(0.0)
    velocidade = float(0.0)
    distancia = float(0.0)
    
    aceleracao = float(input())
    tempo = float(input())
    
    velocidade = aceleracao * tempo
    distancia = (aceleracao * tempo ** 2) / 2
    
    print(f'{velocidade:.1f} m/s e {distancia:.1f} m')
    
    return 0

if __name__ == "__main__":
    main()