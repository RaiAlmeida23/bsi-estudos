"""

Desenvolva um algoritmo que leia quatro números em ponto flutuante representando as coordenadas cartesianas de dois pontos distintos: x1, y1, x2 e y2, informados obrigatoriamente nessa ordem (um por linha). 
O programa deve calcular a distância euclidiana entre eles utilizando a fórmula geométrica:

dab=(x2−x1)2+(y2−y1)2−−−−−−−−−−−−−−−−−−−√

"""

def main():
    x1 = float(0.0)
    y1 = float(0.0)
    x2 = float(0.0)
    y2 = float(0.0)
    d = float(0.0)
    
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    
    d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    
    print(f'A distância entre os pontos ({x1:.1f},{y1:.1f}) e ({x2:.1f},{y2:.1f}) é {d:.2f}.')
    return 0
    
if __name__ == "__main__":
    main()