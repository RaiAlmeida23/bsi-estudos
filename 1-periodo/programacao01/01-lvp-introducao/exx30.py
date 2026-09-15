"""

Desenvolva um algoritmo que leia o tamanho de um arquivo para download em Megabytes (MB) e a velocidade de um link de Internet em Megabits por segundo (Mbps), inseridos um por linha. 
O programa deve calcular e exibir o tempo aproximado para a conclusão do download em segundos.

"""

def main():
    tam = int(0)
    vel = int(0)
    
    tem = float(0.0)
    
    tam = int(input())
    vel = int(input())
    
    tem = (tam * 8) / vel
    
    print(f'{tem:.2f} segundos')
    
    return 0
    
if __name__ == "__main__":
    main()