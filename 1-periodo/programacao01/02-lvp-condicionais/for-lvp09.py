"""

Um jogo de videogame gera um relatório após processar os dados de um campeonato. Neste campeonato vários jogadores participam de 10 fases, onde os pontos são contabilizados por tipos de erros e tipos de acertos para cada fase. Os acertos são caracterizados pelas strings: A1, A2 e A3. Já os erros são caracterizados pelas strings: E1, E2, E3.

Tabela de Pontuação:
- A1 – soma 5 pontos
- A2 – soma 7 pontos
- A3 – soma 10 pontos
- E1 – subtrai 2 pontos, se tiver pontos > 0
- E2 – subtrai 5 pontos, se tiver pontos > 0
- E3 – zera a pontuação atual

Regras Adicionais:
- Os dados são fornecidos nesta ordem: Nick name do jogador e Tipo de erro/acerto para cada uma das 10 fases.
- Considere que os dados encerram quando um nick name igual a string vazia ("") for fornecido.
- Toda vez que a pontuação se tornar negativa, ela deverá ser zerada imediatamente.

"""

def main():
    nick = str("")
    tipo = str("")
    pontos = int(0)
    rodada = int(0)
    total_pontos = int(0)
    qtd_jogadores = int(0)
    melhor_nick = str("")
    melhor_pontos = int(-1)
    
    nick = input()
    
    while(nick != ''):
        pontos = 0
        
        for rodada in range(0, 10, 1):
            tipo = input()
            if(tipo == 'A1'):
                pontos = pontos + 5
                
            elif(tipo == 'A2'):
                pontos = pontos + 7
            
            elif(tipo == 'A3'):
                pontos = pontos + 10
            
            elif(tipo == 'E1'):
                if (pontos > 2):
                    pontos = pontos - 2
                else:
                    pontos = 0
            
            elif(tipo == 'E2'):
                if(pontos >= 5):
                    pontos = pontos - 5
                else:
                    pontos = 0
                    
            elif(tipo == 'E3'):
                pontos = 0
        
        print(nick, pontos, "pontos")
        
        total_pontos = total_pontos + pontos
        qtd_jogadores = qtd_jogadores + 1
        
        if(pontos > melhor_pontos):
            melhor_pontos = pontos
            melhor_nick = nick
            
        nick = input()
    
    if(qtd_jogadores > 0):
        media = total_pontos / qtd_jogadores
        print(f"Média de pontos = {media:.2f} por jogo")
        print("Vencedor", melhor_nick, "com", melhor_pontos, "pontos")
    
    return 0
    
if __name__ == "__main__":
    main()