"""

mplementar uma calculadora funcional baseada em um menu de operações (1 a 6). Fluxo de Execução Obrigatório:

1) Dado o menu de opções (1 a 6) e solicite a escolha do usuário.
2) Validação Prévia: O programa só deve solicitar a entrada de valores numéricos e realizar cálculos se, e somente se, 
a opção selecionada for válida.
3) Caso a opção seja inválida, exiba uma mensagem de erro e encerre a execução imediatamente.

"""

def main():
    operacao = int(0)
    num1 = int(0)
    num2 = int(0)
    
    operacao = int(input())
    
    if(operacao >= 1 and operacao <= 6):
        num1 = int(input())
        num2 = int(input())
        
        if(operacao == 1):
            print(f'{num1 + num2}')
        
        elif(operacao == 2):
            print(f'{num1 - num2}')
        
        elif(operacao == 3):
            print(f'{num1 * num2}')
                
        elif(operacao == 4):
            print(f'{num1 / num2}')
                
        elif(operacao == 5):
            print(f'{num1 ** num2}')
            
        elif(operacao == 6):
            print(f'{num1**(1/num2)}')
    else:
        print(f'OPERACAO INVALIDA')
    
    return 0

if __name__ == "__main__":
    main()